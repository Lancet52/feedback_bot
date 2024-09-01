import os
from html import entities

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

router_handlers = Router()


@router_handlers.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здравствуйте!\n\nНапишите ваш вопрос и мы ответим Вам в ближайшее время.')


@router_handlers.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"""Отправляйте сообщение, фото, видео или документ прямо в чат.\n\nАдминистрация ресурса свяжется с вами обязательно.""")


@router_handlers.message(F.text)
async def text_in(message: Message):
    await message.bot.send_message(chat_id=os.getenv('ADMIN_ID'),
                                   text=message.html_text + f"\n\nСообщение от: #id{message.from_user.id}\n<b>Никнейм:</b> @{message.from_user.username}\n<b>Имя:</b> {message.from_user.first_name}\n<b>Фамилия:</b> {message.from_user.last_name}",
                                   parse_mode="html")


@router_handlers.message(F.photo)
async def photo_in(message: Message):
    await message.bot.send_photo(chat_id=os.getenv('ADMIN_ID'), photo=message.photo[-1].file_id,
                                 caption=message.html_text + f"\n\nСообщение от: #id{message.from_user.id}\n<b>Никнейм:</b> @{message.from_user.username}\n<b>Имя:</b> {message.from_user.first_name}\n<b>Фамилия:</b> {message.from_user.last_name}",
                                 parse_mode="html")


@router_handlers.message(F.video)
async def video_in(message: Message):
    await message.bot.send_video(chat_id=os.getenv('ADMIN_ID'), video=message.video.file_id,
                                 caption=message.html_text + f"\n\nСообщение от: #id{message.from_user.id}\n<b>Никнейм:</b> @{message.from_user.username}\n<b>Имя:</b> {message.from_user.first_name}\n<b>Фамилия:</b> {message.from_user.last_name}",
                                 parse_mode="html")


@router_handlers.message(F.document)
async def doc_in(message: Message):
    await message.bot.send_document(chat_id=os.getenv('ADMIN_ID'), document=message.document.file_id,
                                    caption=message.html_text + f"\n\nСообщение от: #id{message.from_user.id}\n<b>Никнейм:</b> @{message.from_user.username}\n<b>Имя:</b> {message.from_user.first_name}\n<b>Фамилия:</b> {message.from_user.last_name}",
                                    parse_mode="html")
