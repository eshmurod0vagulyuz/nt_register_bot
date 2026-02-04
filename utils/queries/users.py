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


async def add_user(language: str, message: types.Message) -> bool | None:
    try:
        query = """
            INSERT INTO users (chat_id,username, language)
            VALUES (%s,%s,%s,)
        """
        params: tuple[int, str, str] = (message.from_user.id, message.from_user.username, language)


        execute_query(query=query, params=params)
        return True
    except Exception as e:
        logger.error(msg=e)
        return None


async def update_user(data: dict, message: types.Message) -> bool | None:
    try:
        full_name=data.get("full_name")
        phone_number = data.get("phone_number")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        query = """
            UPDATE users SET full_name=%s, phone_number=%s, latitude=%s, longitude=%s 
            WHERE chat_id=%s
        """
        params=(full_name, phone_number, latitude, longitude, message.from_user.id )

        execute_query(query=query, params=params)
        return True
    except Exception as e:
        logger.error(msg=e)
        return None