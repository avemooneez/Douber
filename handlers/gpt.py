from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters.command import CommandObject
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
import requests
import uuid
import json
from utils import tokens, gigachat

router = Router()
router.message.filter(F.chat.type.in_({"private"}))
auth = tokens.sber_id

class GigaChat(StatesGroup):
    response = State()

response = gigachat.get_token(auth)
if response != 1:
  print(response.text)
  giga_token = response.json()['access_token']
url = "https://gigachat.devices.sberbank.ru/api/v1/models"
payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {giga_token}'
}
response = requests.request("GET", url, headers=headers, data=payload, verify=False)


@router.message(StateFilter(None), Command("gpt_giga"))
async def cmd_gpt(message: Message, state: FSMContext):
    await message.reply("Диалог с GigaChat начат. Закончить — /cancel")
    await state.set_state(GigaChat.response)


@router.message(GigaChat.response)
async def cmd_gpt_cycle(message: Message, state=FSMContext):
    if message.text == "/cancel":
        state.clear()
        await message.answer("Диалог с GigaChat окончен.")
        await state.set_state(None)
        return
    if 'conversation_history' not in globals() or 'response' not in globals():
        global conversation_history, response
        response, conversation_history = gigachat.get_chat_completion(giga_token, message.text)
    else:
        response, conversation_history = gigachat.get_chat_completion(giga_token, message.text, conversation_history)
    response = f"{response.json()['choices'][0]['message']['content']}"
    try:
        await message.reply(f"{response}", parse_mode=ParseMode.MARKDOWN)
    except:
        await message.reply(f"{response}", parse_mode=ParseMode.HTML)
    await state.set_state(GigaChat.response)
