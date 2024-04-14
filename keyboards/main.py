from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(
        InlineKeyboardButton(text="Настройки", callback_data="settings"),
        InlineKeyboardButton(text="Крипта", callback_data="crypto")
    )
    kb.row(
        InlineKeyboardButton(text="Языковая модель", callback_data="chatbot")
        )
    kb.row(
        InlineKeyboardButton(text="Закрыть", callback_data="close")
        )
    return kb.as_markup(resize_keyboard=True)