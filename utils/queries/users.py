import logging

from aiogram import types

from core.db_setting import execute_query

logger = logging.getLogger(__name__)


async def get_user(chat_id: int) -> dict | None:
    try:
        query = "SELECT * FROM users WHERE chat_id=%s"
        params: tuple[int] = (chat_id,)

        user = execute_query(query=query, params=params, fetch='one')
        return user
    except Exception as e:
        logger.error(e)
        return None


async def add_user(data: dict, message: types.Message) -> bool | None:
    try:
        query = """
            INSERT INTO users (chat_id,username,full_name,language,
            phone_number,longitude,latitude) VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        params: tuple[int, str, str, str, str, str, str] = (message.from_user.id, message.from_user.username,
                                                            data.get("full_name"),
                                                            data.get('language'), data.get('phone_number'),
                                                            data.get('longitude'), data.get('latitude'),)

        execute_query(query=query, params=params)
        return True
    except Exception as e:
        logger.error(msg=e)
        return None