from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text="Крипта"),
        KeyboardButton(text="Языковая модель")
    )
    kb.row(
        KeyboardButton(text="Настройки"),
        KeyboardButton(text="Помощь")
        )
    kb.row(
        KeyboardButton(text="О боте"),
        KeyboardButton(text="Донат")
    )
    kb.row(
        KeyboardButton(text="Закрыть")
    )
    return kb.as_markup(resize_keyboard=True)