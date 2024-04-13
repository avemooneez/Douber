from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_setings() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Crypto", callback_data="crypto_st")
    kb.adjust(2)
    kb.button(text="Назад", callback_data="main")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
