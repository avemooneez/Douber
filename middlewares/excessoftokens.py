from typing import Any, Awaitable, Callable, Dict
from aiogram.types import Message, TelegramObject
from aiogram import BaseMiddleware
from keyboards import main
from db import Database

db = Database("./database.db")

class ExcessOfTokens(BaseMiddleware):

    def __init__(self):
        pass

    async def __call__(self,
                       handler: Callable[[TelegramObject,Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        used_tokens = db.get_used_tokens(event.from_user.id)
        if used_tokens[0][0] >= 50000:
            return await event.answer("Токены закончились! Чтобы получить больше токенов необходимо поддержать проект, а скриншот о донате отправить @mnz_pr.",
                                      reply_markup=main.main_kb())
        return await handler(event, data)
