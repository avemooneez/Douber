from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram import Router, F
from keyboards.geolocation import geolocation
from utils import geo


router = Router()

@router.message(Command("timezone"))
async def cmd_geo(message: Message):
    await message.reply("Отправь мне свою геолокацию.", reply_markup=geolocation())

@router.message(F.location)
async def on_location(message: Message):
    # await message.reply(f"{message.location.longitude}, {message.location.latitude}")
    await message.answer(geo.tz(lon=message.location.longitude, lat=message.location.latitude))