from aiogram.types import Message
from aiogram import Router, F

router = Router()

@router.message(F.text == "Донат")
async def cbq_crypto(message: Message):
    await message.reply("BTC: ```1AdDq1DfvzxRzWwfMdss1392pSqZKfLbY1```\n"
                        "USDT TRC20: ```TQCivxEGG32st2P7dDce4cqNTkcFxksexw```\n"
                        "DonationAlerts: donationalerts.com/r/avemooneez\n"
                        "Сбор Тинькофф: tinkoff.ru/cf/fou6EWkgYB\n",
                        disable_web_page_preview=True)
