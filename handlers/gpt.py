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
router = Router()

class ChatCPT(StatesGroup):
    response = State()

@router.message(StateFilter(None), F.text == "Языковая модель")
async def cmd_gpt(message: Message, state: FSMContext):
    used_tokens = db.get_used_tokens(message.from_user.id)
    router.message.middleware(middleware=ExcessOfTokens(used_tokens))

    await message.answer(text="Принято!", reply_markup=ReplyKeyboardRemove())
    await message.bot.delete_message(message.chat.id, message.message_id + 1)
    await message.reply("Диалог с ChatGPT начат", reply_markup=back.back())
    await state.set_state(ChatCPT.response)

@router.callback_query(F.data == "main")
async def close(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Диалог с ChatGPT окончен.", reply_markup=main.main_kb())
    await callback.answer()
    await state.set_state(None)
    return

@router.message(ChatCPT.response)
async def cmd_gpt_cycle(message: Message, state=FSMContext):
    used_tokens = db.get_used_tokens(message.from_user.id)
    router.message.middleware(middleware=ExcessOfTokens(used_tokens))
    
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
            reply_markup=back.back()
            )
    except:
        await message.reply(
            f"{response}",
            parse_mode=ParseMode.HTML,
            reply_markup=back.back()
            )
        
    await state.set_state(ChatCPT.response)