from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from utils.urlshort import short_url


router = Router()

class ShortURL(StatesGroup):
    short = State()

@router.message(StateFilter(None), F.text == "Сократить ссылку")
async def cmd_url(message: Message, state: FSMContext):
    await message.reply("Введите ссылку")
    await state.set_state(ShortURL.short)

@router.message(ShortURL.short)
async def response(message: Message, state: FSMContext):
    url = short_url(url=message.text)
    if url != "Please enter a valid URL.":
        await message.reply(url)
    else:
        await message.reply("К сожалению, ссылка не валидна. Попробуйте ещё раз")
    await state.set_state(None)
    return
