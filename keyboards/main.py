from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text="Крипта"),
        KeyboardButton(text="Языковая модель")
    )
    kb.row(
        KeyboardButton(text="Настройки")
        )
    kb.row(
        KeyboardButton(text="О боте")
    )
    return kb.as_markup(resize_keyboard=True)