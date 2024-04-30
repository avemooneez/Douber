import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from utils import tokens, reset_limit
from handlers import start, support, crypto, settings, about, gpt, donate, profile, urlshort
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from db import Database

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    db = Database("./database.db")
    db.start()
    
    bot = Bot(token=tokens.bot_token)
    dp = Dispatcher()
    
    dp.include_routers(
        start.router, 
        crypto.router_crypto, 
        settings.router, 
        about.router, 
        gpt.router_gpt, 
        support.router, 
        donate.router,
        profile.router,
        urlshort.router
        )
    
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(reset_limit.main, trigger="cron", day="1", start_date="2024-04-01 00:00:00")
    scheduler.start()
    
    dp.message.filter(F.chat.type.in_({"private"}))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())