from statistics import median

from aiogram import Router

from handlers import start, chats


def include_routers():
    main_router = Router()
    main_router.include_router(start.router)
    main_router.include_router(chats.router)

    return main_router