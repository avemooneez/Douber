from aiogram.types import Message
from aiogram import Router, F
from aiogram.enums import ParseMode

router = Router()

@router.message(F.text == "Донат")
async def cbq_crypto(message: Message):
    await message.reply(
        """BTC: `1AdDq1DfvzxRzWwfMdss1392pSqZKfLbY1`
USDT TRC20: `TQCivxEGG32st2P7dDce4cqNTkcFxksexw`
DonationAlerts: donationalerts.com/r/avemooneez
Сбор Тинькофф: tinkoff.ru/cf/fou6EWkgYB""",
                        disable_web_page_preview=True,
                        parse_mode=ParseMode.MARKDOWN)