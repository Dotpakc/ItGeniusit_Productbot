import logging

async def on_start(dp):
    logging.info('Starting bot')
    

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_start)