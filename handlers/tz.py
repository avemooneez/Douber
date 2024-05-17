from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import geolocation, main
from utils import geo
import datetime
import pytz


router = Router()

@router.message(Command("timezone"))
async def cmd_geo(message: Message):
    await message.reply("Отправь мне свою геолокацию.", reply_markup=geolocation.geolocation())

@router.message(F.location)
async def on_location(message: Message):
    timezone = geo.tz(lon=message.location.longitude, lat=message.location.latitude)
    time = datetime.datetime.now(tz=pytz.timezone(timezone)).strftime("%H:%M")
    await message.answer(f"🌍 Ваш часовой пояс: {timezone}\n"
                         f"🕐 Ваше время: {time}", reply_markup=main.main_kb()
                         )