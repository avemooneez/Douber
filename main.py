import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from handlers import start, help, crypto, settings, about
from db import Database

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    db = Database("./database.db")
    db.start()
    load_dotenv(find_dotenv())
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    
    dp.include_routers(start.router, help.router, crypto.router, settings.router, about.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())