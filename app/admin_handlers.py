import os
from html import entities

from aiogram import F, Router
from aiogram.types import Message

router_adminhandlers = Router()


@router_adminhandlers.message(F.reply_to_message)
async def reply_to_user(message: Message):
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
            await message.bot.send_message(chat_id=user_id, text=message.text)
