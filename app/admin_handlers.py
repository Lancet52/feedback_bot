import os
from html import entities

from aiogram import F, Router
from aiogram.types import Message

router_adminhandlers = Router()


@router_adminhandlers.message(F.reply_to_message)

async def reply_to_user_text(message: Message):
    entities = message.reply_to_message.entities or message.reply_to_message.caption_entities
    if not entities or entities[0].type != "hashtag":
        raise ValueError("Не удалось извлечь ID для ответа!")
        pass
    else:
        hashtag = entities[0].extract_from(message.reply_to_message.text or message.reply_to_message.caption)
        if len(hashtag) < 4 or not hashtag[3:].isdigit():
            raise ValueError("Некорректный ID для ответа!")
        else:
            user_id = hashtag[3:]
            if message.text:
                await message.bot.send_message(chat_id=user_id, text=message.text)
            elif message.photo:
                await message.bot.send_photo(chat_id=user_id, photo=message.photo[-1].file_id, caption=message.caption)
            elif message.video:
                await message.bot.send_video(chat_id=user_id, video=message.video.file_id, caption=message.caption)
            elif message.document:
                await message.bot.send_document(chat_id=user_id, document=message.document.file_id, caption=message.caption)
            else:
                print('Данный формат файла не поддерживается!')

