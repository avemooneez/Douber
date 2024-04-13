import asyncio
import logging
from aiogram import Bot, Dispatcher
from utils import tokens
from handlers import start, help, crypto, settings, about, gpt
from db import Database

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    db = Database("./database.db")
    db.start()
    
    bot = Bot(token=tokens.bot_token)
    dp = Dispatcher()
    
    dp.include_routers(start.router, help.router, crypto.router, settings.router, about.router, gpt.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())