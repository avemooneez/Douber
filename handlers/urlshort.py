from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from utils.urlshort import short_url
from db import Database

router = Router()
db = Database("./database.db")

class GetURL(StatesGroup):
    get_url = State()

@router.message(StateFilter(None), Command("url"))
async def cmd_urlshort(message: Message, state: FSMContext):
    await message.reply(
        "Введите ссылку..."
    )
    await state.set_state(GetURL.get_url)

@router.message(StateFilter(GetURL.get_url))
async def urlshort(message: Message, state: FSMContext):
    url = short_url(url=message.text)
    if url != "Please enter a valid URL.":
        await message.reply(url)
        await state.set_state(None)
        return
    else:
        await message.reply("Пожалуйста, введите валидную ссылку")
        await state.set_state(GetURL.get_url)
