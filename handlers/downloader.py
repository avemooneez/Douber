from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandObject
from aiogram import Router, F
from aiogram.enums import ParseMode
from utils.youtubedownload import download
from os import remove
from aiogram import exceptions


router = Router()

@router.message(Command("download"))
async def cmd_download(message: Message, command: CommandObject):
    if command.args == None:
        await message.reply(
            "Неверное использование: /download <ссылка>"
        )
        return
    await message.answer("Запрос принят, видео загружается!")
    ytname = download(command.args)
    if ytname == "Exception":
        await message.bot.delete_message(message.chat.id, message.message_id + 1)
        await message.answer("Неизвестная ошибка.")
        return
    try:
        ytvid = FSInputFile(f"./temp/{ytname}")
        await message.bot.delete_message(message.chat.id, message.message_id + 1)
        await message.answer_video(ytvid)
        remove(f"./temp/{ytname}")
    except exceptions.TelegramEntityTooLarge:
        await message.answer("К сожалению, файл слишком большой.")
        remove(f"./temp/{ytname}")
    except Exception:
        await message.answer("Неизвестная ошибка.")
