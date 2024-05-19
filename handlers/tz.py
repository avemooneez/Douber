from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import geolocation, main
from utils import geo
import datetime
import pytz
from db import Database


router = Router()
db = Database("./database.db")

@router.callback_query(F.data == "timezone_st")
async def cmd_geo(callback: CallbackQuery):
    await callback.message.answer(
        "🌍 Для корректной работы боту необходимо знать ваш часовой пояс. Пожалуйста, отправьте ваше местоположение.",
        reply_markup=geolocation.geolocation()
        )
    await callback.answer()

@router.message(F.location)
async def on_location(message: Message):
    timezone = geo.tz(lon=message.location.longitude, lat=message.location.latitude)
    time = datetime.datetime.now(tz=pytz.timezone(timezone)).strftime("%H:%M")
    await message.answer(f"🌍 Ваш часовой пояс: {timezone}\n"
                         f"🕐 Ваше время: {time}",
                         reply_markup=main.main_kb()
                         )
    db.add_tz(timezone, message.from_user.id)