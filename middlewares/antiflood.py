from typing import Any, Awaitable, Callable, Dict
from aiogram.types import Message, TelegramObject
from aiogram import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage


class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, storage: RedisStorage, limit):
        self.storage = storage
        self.limit = limit
    
    async def __call__(self,
                       handler: Callable[[TelegramObject,Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        user = f"user{event.from_user.id}"

        check_user = await self.storage.redis.get(name=user)
        if check_user:
            if int(check_user.decode()) == 1:
                return await event.answer("Пиши медленнее!")
            return
        await self.storage.redis.set(name=user, value=1, ex=self.limit)

        return await handler(event, data)
