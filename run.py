import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.admin_handlers import router_admin_handlers
from app.handlers import router_user_handlers


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router_admin_handlers, router_user_handlers)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('БОТ ЗАПУЩЕН')
        asyncio.run(main())

    except KeyboardInterrupt:
        print('БОТ ВЫКЛЮЧЕН')
