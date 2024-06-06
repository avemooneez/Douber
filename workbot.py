from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from db import Database


router = Router()
db = Database("./database.db")

@router.message(Command("post"), F.chat.id == 1699948729)
async def cmd_start(message: Message):
    users = db.get_users()
    for i in range(len(users)):
        await message.bot.send_message(chat_id=users[i][0], text=
"""<b>Обновление </b>#Douber<b>!</b>

<b>[+]</b> Подключен <b>сократитель ссылок</b> <code>clc.li</code>
<i><tg-spoiler><b>[</b>О боте </tg-spoiler></i><i><tg-spoiler><b>→</b> Сократить ссылку</tg-spoiler></i><b><i><tg-spoiler>]</tg-spoiler></i></b>
<b>[+]</b> Добавлен <b>контекст</b> и возможность его сброса в <b>ChatGPT</b>
<b>[+]</b> Добавлен <b>профиль</b>, показывающий версию и количество токенов
<b>[+]</b> Добавлена возможность <b>поддержать разработчиков</b>
<i><tg-spoiler><b>[</b>О боте </tg-spoiler></i><i><tg-spoiler><b>→</b> Донат</tg-spoiler></i><b><i><tg-spoiler>]</tg-spoiler></i></b>
<b>[~] </b>Установлен лимит в <b>50 000</b> токенов
<b>[=]</b> Добавляется установка <b>часового пояса</b>
<i><tg-spoiler><b>[</b>Настройки → Часовой пояс</tg-spoiler></i><b><i><tg-spoiler>]</tg-spoiler></i></b>

<a href='http://t.me/tivehive'><b>TiveHive в Телеграм</b></a>""",
                         parse_mode="html",
                         disable_web_page_preview=True)
    
