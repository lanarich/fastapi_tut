from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.predict_item_kb import predict_item_keyboard

router_start = Router()

@router_start.message(Command(commands='start'))
async def get_started(message: Message, bot:Bot):
    await bot.send_sticker(message.from_user.id, sticker= 'CAACAgIAAxkBAAELQXVltL8IbUllavWAXg94LVoSEgnkCgAClBgAAvdbgEjPGPx-6kVXrjQE')
    await bot.send_message(message.from_user.id, f'Доброго времени суток \n'
                                                 f'Это бот для ветеринарной клиники! \n\n\n', reply_markup= predict_item_keyboard)

