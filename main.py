import asyncio  # Работа с асинхронностью
from handler.common import common_router
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from config import config  # Config


def register_all_routers(dp: Dispatcher):
    dp.include_router(common_router)


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(storage=MemoryStorage())  # Менеджер бота

    register_all_routers(dp)

    try:
        print('Bot Started')
        await dp.start_polling(bot)



    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')