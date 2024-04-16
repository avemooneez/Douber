from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text="Помощь"),
        KeyboardButton(text="Донат")
    )
    kb.row(
        KeyboardButton(text="Закрыть")
    )
    return kb.as_markup(resize_keyboard=True)