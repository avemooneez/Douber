from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
import requests
import uuid
import json
from utils import tokens, chatgpt


router = Router()

class ChatCPT(StatesGroup):
    response = State()

@router.message(StateFilter(None), Command("gpt"))
async def cmd_gpt(message: Message, state: FSMContext):
    await message.reply("Диалог с ChatGPT начат.\nЗакончить — /cancel")
    await state.set_state(ChatCPT.response)

@router.message(ChatCPT.response)
async def cmd_gpt_cycle(message: Message, state=FSMContext):
    if message.text == "/cancel":
        await message.answer("Диалог с ChatGPT окончен.")
        await state.set_state(None)
        return
    try:
        await message.reply(
            f"{chatgpt.get_chat_completion(user_message=message.text)}",
            parse_mode=ParseMode.MARKDOWN
            )
    except:
        await message.reply(
            f"{chatgpt.get_chat_completion(user_message=message.text)}",
            parse_mode=ParseMode.HTML
            )
    await state.set_state(ChatCPT.response)