import asyncio,sys
from aiogram import Bot,Dispatcher
from bot.handlers import client
from bot.create_bot import bot,dp 
from info import models

print(sys.path)
sys.path.append("/path/to/Telegram bot/__!__/info")

async def main():
    print('Bot online....')
    dp.include_router(handlers.client.router)
    await dp.start_polling(bot,close_bot_session=True) 


    






if __name__=='__main__':
    asyncio.run(main())