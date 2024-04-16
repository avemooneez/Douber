from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_setings() -> InlineKeyboardMarkup:
    ReplyKeyboardRemove()
    kb = InlineKeyboardBuilder()
    kb.button(text="Crypto", callback_data="crypto_st")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
