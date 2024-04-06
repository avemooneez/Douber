from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import Database

db = Database("./database.db")

def get_cryptos(user_id) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    selectedCryptos = db.get_selectedCryptos(user_id)
    # BTC
    if selectedCryptos[0][0] == 1:
        kb.button(text="✅ BTC / Bitcoin", callback_data="BTCUSDT")
    elif selectedCryptos[0][0] == 0:
        kb.button(text="BTC / Bitcoin", callback_data="BTCUSDT")
    
    # ETH
    if selectedCryptos[0][1] == 1:
        kb.button(text="✅ ETH / Ethereum", callback_data="ETHUSDT")
    elif selectedCryptos[0][1] == 0:
        kb.button(text="ETH / Ethereum", callback_data="ETHUSDT")
    
    # TON
    if selectedCryptos[0][2] == 1:
        kb.button(text="✅ TON / Toncoin", callback_data="TONUSDT")
    elif selectedCryptos[0][2] == 0:
        kb.button(text="TON / Toncoin", callback_data="TONUSDT")

    # SOL
    if selectedCryptos[0][3] == 1:
        kb.button(text="✅ SOL / Solana", callback_data="SOLUSDT")
    elif selectedCryptos[0][3] == 0:
        kb.button(text="SOL / Solana", callback_data="SOLUSDT")
    
    # ADA
    if selectedCryptos[0][4] == 1:
        kb.button(text="✅ ADA / Cardano", callback_data="ADAUSDT")
    elif selectedCryptos[0][4] == 0:
        kb.button(text="ADA / Cardano", callback_data="ADAUSDT")
    
    # DOGE
    if selectedCryptos[0][5] == 1:
        kb.button(text="✅ DOGE / Dogecoin", callback_data="DOGEUSDT")
    elif selectedCryptos[0][5] == 0:
        kb.button(text="DOGE / Dogecoin", callback_data="DOGEUSDT")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
