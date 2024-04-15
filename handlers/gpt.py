from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from utils import chatgpt

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
    
    if 'conversation_history' not in globals():
        global conversation_history
        conversation_history = []
        response = chatgpt.get_chat_completion(message.text, conversation_history)
    elif 'conversation_history' in globals():
        response = chatgpt.get_chat_completion(message.text, conversation_history)
        
    try:
        await message.reply(
            f"{response}",
            parse_mode=ParseMode.MARKDOWN
            )
    except:
        await message.reply(
            f"{response}",
            parse_mode=ParseMode.HTML
            )
        
    await state.set_state(ChatCPT.response)