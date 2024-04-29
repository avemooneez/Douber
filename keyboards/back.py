from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def back_first() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Закончить диалог", callback_data="main")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def back_second() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Сбросить контекст", callback_data="reset_context")
    kb.button(text="Закончить диалог", callback_data="main")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)