import requests
import datetime
from db import Database

db = Database("./database.db")

def get_message(user_id):
    time_now_utc3 = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)).strftime('%H:%M:%S')
    msg = f"Текущее время: UTC+3/MSK {time_now_utc3}"
    selectedCryptos = db.get_selectedCryptos(user_id)
    if selectedCryptos[0][0] == 1:
        url = "https://api.coingecko.com/api/v3/coins/binance-bitcoin"
        responce = requests.get(url)
        data = responce.json()
        price = data.get("market_data").get("current_price").get("usd")
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

    return msg