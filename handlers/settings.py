from aiogram.types import CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from keyboards import settings, crypto, main
from db import Database

router = Router()
db = Database("./database.db")

class Settings(StatesGroup):
    choosing_crypto = State()

@router.callback_query(F.data == "main")
async def edit_kb(callback: CallbackQuery):
    await callback.message.edit_text(
"""Привет! Это — бот-помощник от компании <b><a href="https://t.me/tivehive">TiveHive</a></b>.
Воспользуйся кнопками ниже для управления ботом""",
                         reply_markup=main.main_kb(),
                         parse_mode="html",
                         disable_web_page_preview=True)

@router.callback_query(F.data == "settings")
async def edit_kb(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите что вы хотите настроить...",
        reply_markup=settings.get_setings()
    )

@router.callback_query(F.data == "crypto_st")
async def answer_crypto(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите криптовалюты для отображения",
        reply_markup=crypto.get_cryptos(callback.from_user.id)
    )

@router.callback_query(F.data == "BTCUSDT")
async def edit_kb(callback: CallbackQuery):
    try:
        OnOff = db.get_selectedCryptos(callback.from_user.id)
        if OnOff[0][0] == 1:
            OnOff = 0
        elif OnOff[0][0] == 0:
            OnOff = 1
        db.edit_selectedCryptos(callback.from_user.id, "BTC", OnOff)
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=crypto.get_cryptos(callback.from_user.id)
            )
    except:
        await callback.answer("Unknown error. Please, try again")

@router.callback_query(F.data == "ETHUSDT")
async def edit_kb(callback: CallbackQuery):
    try:
        OnOff = db.get_selectedCryptos(callback.from_user.id)
        if OnOff[0][1] == 1:
            OnOff = 0
        elif OnOff[0][1] == 0:
            OnOff = 1

        db.edit_selectedCryptos(callback.from_user.id, "ETH", OnOff)
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=crypto.get_cryptos(callback.from_user.id)
            )
    except:
        await callback.answer("Unknown error. Please, try again")

@router.callback_query(F.data == "TONUSDT")
async def edit_kb(callback: CallbackQuery):
    try:
        OnOff = db.get_selectedCryptos(callback.from_user.id)
        if OnOff[0][2] == 1:
            OnOff = 0
        elif OnOff[0][2] == 0:
            OnOff = 1

        db.edit_selectedCryptos(callback.from_user.id, "TON", OnOff)
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=crypto.get_cryptos(callback.from_user.id)
            )
    except:
        await callback.answer("Unknown error. Please, try again")

@router.callback_query(F.data == "SOLUSDT")
async def edit_kb(callback: CallbackQuery):
    try:
        OnOff = db.get_selectedCryptos(callback.from_user.id)
        if OnOff[0][3] == 1:
            OnOff = 0
        elif OnOff[0][3] == 0:
            OnOff = 1

        db.edit_selectedCryptos(callback.from_user.id, "SOL", OnOff)
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=crypto.get_cryptos(callback.from_user.id)
            )
    except:
        await callback.answer("Unknown error. Please, try again")

@router.callback_query(F.data == "ADAUSDT")
async def edit_kb(callback: CallbackQuery):
    try:
        OnOff = db.get_selectedCryptos(callback.from_user.id)
        if OnOff[0][4] == 1:
            OnOff = 0
        elif OnOff[0][4] == 0:
            OnOff = 1

        db.edit_selectedCryptos(callback.from_user.id, "ADA", OnOff)
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=crypto.get_cryptos(callback.from_user.id)
            )
    except:
        await callback.answer("Unknown error. Please, try again")

@router.callback_query(F.data == "DOGEUSDT")
async def edit_kb(callback: CallbackQuery):
    try:
        OnOff = db.get_selectedCryptos(callback.from_user.id)
        if OnOff[0][5] == 1:
            OnOff = 0
        elif OnOff[0][5] == 0:
            OnOff = 1

        db.edit_selectedCryptos(callback.from_user.id, "DOGE", OnOff)
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=crypto.get_cryptos(callback.from_user.id)
            )
    except:
        await callback.answer("Unknown error. Please, try again")
