from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from middlewares.excessoftokens import ExcessOfTokens
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from keyboards import main, back
from db import Database
from utils import chatgpt


db = Database("./database.db")
router_gpt = Router()
router_gpt.message.middleware(middleware=ExcessOfTokens())

class ChatCPT(StatesGroup):
    response = State()

@router_gpt.message(StateFilter(None), F.text == "Языковая модель")
async def cmd_gpt(message: Message, state: FSMContext):
    await message.answer(text="Принято!", reply_markup=ReplyKeyboardRemove())
    await message.bot.delete_message(message.chat.id, message.message_id + 1)
    await message.reply("Диалог с ChatGPT начат", reply_markup=back.back_first())
    await state.set_state(ChatCPT.response)

@router_gpt.callback_query(F.data == "main")
async def close(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Диалог с ChatGPT окончен.", reply_markup=main.main_kb())
    await callback.answer()
    await state.set_state(None)
    return

@router_gpt.callback_query(F.data == "reset_context")
async def reset_context(callback: CallbackQuery, state: FSMContext):
    global conversation_history
    conversation_history = []
    await callback.message.answer("Контекст был перезагружен, приятного пользования!")
    await callback.answer()
    await state.set_state(ChatCPT.response)

@router_gpt.message(ChatCPT.response)
async def cmd_gpt_cycle(message: Message, state=FSMContext):
    if 'conversation_history' not in globals():
        global conversation_history
        conversation_history = []
        response = chatgpt.get_chat_completion(message.from_user.id, message.text, conversation_history)
    elif 'conversation_history' in globals():
        response = chatgpt.get_chat_completion(message.from_user.id, message.text, conversation_history)
        
    try:
        await message.reply(
            f"{response}",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=back.back_second()
            )
    except:
        await message.reply(
            f"{response}",
            parse_mode=ParseMode.HTML,
            reply_markup=back.back_second()
            )
        
    await state.set_state(ChatCPT.response)