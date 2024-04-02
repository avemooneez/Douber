from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import requests
from datetime import datetime
from db import Database

router = Router()
db = Database("./database.db")

@router.message(Command("crypto"))
async def cmd_crypto(message: Message):
    if message.chat.type == 'private':
        #response = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json().get('price')
        #data = response.json()
        #btc_price = data.get('price')
        msg = f"Time: UTC+3 {datetime.now().strftime('%H:%M:%S')}"
        selectedCryptos = db.get_selectedCryptos(message.from_user.id)
        if selectedCryptos[0][0] == 1:
            responce = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            data = responce.json()
            price = data.get('price')
            msg += "".join(f"\nBTC: ${'%0.2f' % float(price)}")
        elif selectedCryptos[0][0] == 0:
            pass

        if selectedCryptos[0][1] == 1:
            responce = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
            data = responce.json()
            price = data.get('price')
            msg += "".join(f"\nETH: ${float(price)}")
        elif selectedCryptos[0][1] == 0:
            pass

        if selectedCryptos[0][2] == 1:
            url = "https://api.coingecko.com/api/v3/coins/the-open-network"
            responce = requests.get(url)
            data = responce.json()
            price = data.get("market_data").get("current_price").get("usd")
            msg += "".join(f"\nTON: ${price}")
        elif selectedCryptos[0][2] == 0:
            pass
        
        if selectedCryptos[0][3] == 1:
            responce = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT")
            data = responce.json()
            price = data.get('price')
            msg += "".join(f"\nSOL: ${float(price)}")
        elif selectedCryptos[0][3] == 0:
            pass

        if selectedCryptos[0][4] == 1:
            responce = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT")
            data = responce.json()
            price = data.get('price')
            msg += "".join(f"\nADA: ${float(price)}")
        elif selectedCryptos[0][4] == 0:
            pass

        if selectedCryptos[0][5] == 1:
            responce = requests.get(url="https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT")
            data = responce.json()
            price = data.get('price')
            msg += "".join(f"\nDOGE: ${float(price)}")
        elif selectedCryptos[0][5] == 0:
            pass
            
        await message.answer(msg)
