from pathlib import Path
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject, User, Update
from babel.support import Translations

I18N_DOMAIN= "messages"
LOCALES_DIR=Path("locales")

class I18NMiddleware(BaseMiddleware):
    translations: dict[Any, Any]

    def __init__(self, locales_dir: Path, domain:str="messages"):
        self.locales_dir = locales_dir
        self.domain = domain
        self.translations={}
        self._load_translations()
        super().__init__()

    def _load_translations(self):
        """Load all translations"""
        for locale_dir in self.locales_dir.iterdir():
            if locale_dir.is_dir():
                locale=locale_dir.name
                try:
                    self.translations[locale]=Translations.load(
                        dirname=str(self.locales_dir),
                        locales=[locale],
                        domain=self.domain,
                    )
                except Exception as e:
                    print(f'Failed to load translation {locale}: {e}')


    def gettext(self, message: str, locale: str=None) -> str:
        if locale and locale in self.translations:
            return self.translations[locale].gettext(message)
        return message


    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        # state: FSMContext = data.get("state")

        if user:
            from utils.queries.users import get_user
            user_data = await get_user(user.id)

            if user_data and 'language' in user_data:
                user_locale = user_data['language']
            else:
                user_locale = 'uz'
                # if state:
                #     state_data = await state.get_data()
                #     locale = state_data.get('language','uz')
                # else:
                # locale = 'uz'

            trans = self.translations.get(user_locale)
            if trans:
                data['i18n'] = trans

                def _(text:str, locale:str=None):
                    if locale:
                        return self.gettext(text, locale)
                    return trans.gettext(text)

                data['_'] = _
            else:
                data['_']=lambda text, locale=None: self.gettext(text, locale) if locale else text

        data['locale'] = user_locale
        data['i18n_middleware'] = self

        # Handlerga faqat event va data uzatamiz, boshqa kalitlar bermaymiz
        return await handler(event, data)


def setup_middleware(dp):
    """Setup i18n middleware"""
    i18n=I18NMiddleware(LOCALES_DIR, I18N_DOMAIN)

    #Register for both messages and callback queries
    dp.message.middleware(i18n)
    dp.callback_query.middleware(i18n)

    return i18n
