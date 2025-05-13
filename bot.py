from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command


api = '7896054597:AAFXSBpGEeKOPMz03Jf76H5vF9aajKtqeMg'
bot = Bot(api)
dp=Dispatcher()

@dp.message(Command('start'))
async def send_salem(sms:types.Message):
    await sms.answer(
         text=f'salem{sms.from_user.first_name}')

@dp.message(Command('info'))
async def send_info(sms:types.Message):
    await sms.reply(text='bul menin botim')


@dp.message(Command('suwret'))
async def send_suwret(sms:types.Message):
    await sms.answer_photo(
        photo=types.FSInputFile(path='Без названия.jfif')
    )
@dp.message()
async def send_error(sms:types.Message):
    await sms.answer(text='tusinbedim, magan basqa zat jazba!')


async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
