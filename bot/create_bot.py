from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, Filter
from information import models

router=Router()

@router.message(Command('start'))
async def run_bot(message:Message):
    data=models.Users.objects.all()
    for i in data:
        await message.answer(f"{i}")

    