from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_setings() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Crypto", callback_data="crypto_st")
    kb.button(text="Закрыть", callback_data="close_st")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
