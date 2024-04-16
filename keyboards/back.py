from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

def back() -> InlineKeyboardMarkup:
    ReplyKeyboardRemove()
    kb = InlineKeyboardBuilder()
    kb.button(text="Закончить диалог", callback_data="main")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)