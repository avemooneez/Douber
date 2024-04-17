from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.enums import ParseMode
from db import Database

router = Router()
db = Database("./database.db")

@router.message(Command("profile"))
@router.message(F.text == "Профиль")
async def cmd_profile(message: Message):
    model = db.get_model(message.from_user.id)
    tokens = db.get_used_tokens(message.from_user.id)
    msg_template = """Профиль @{username}

<i><b>GPT:</b></i>
<b>Модель</b> — <code>{model}</code>
<b>Лимит токенов</b> — {limit} из 50,000
Обновление 1 мая в 00:00 (UTC+3/MSK)

Чтобы получить больше токенов необходимо поддержать проект, а скриншот о донате отправить @mnz_pr."""
    msg = msg_template.format(username=message.from_user.username, model=model[0][0], limit=tokens[0][0])
    await message.reply(f"{msg}", parse_mode=ParseMode.HTML)
