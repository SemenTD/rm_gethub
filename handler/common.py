from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from API.waifu import waifu_api

common_router = Router()


@common_router.message(Command("start"))
async def start_command(message: Message):
    waifu = await waifu_api.get_waifu("cringe")
    await message.answer_photo(waifu)
