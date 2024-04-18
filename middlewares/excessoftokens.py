from typing import Any, Awaitable, Callable, Dict
from aiogram.types import Message, TelegramObject
from aiogram import BaseMiddleware


class ExcessOfTokens(BaseMiddleware):

    def __init__(self, used_tokens):
        self.used_tokens = used_tokens

    async def __call__(self,
                       handler: Callable[[TelegramObject,Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:

        if self.used_tokens[0][0] >= 50000:
            return await event.answer("Токены закончились! Чтобы получить больше токенов необходимо поддержать проект, а скриншот о донате отправить @mnz_pr.")
        return await handler(event, data)
