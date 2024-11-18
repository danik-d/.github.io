import aiogram
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router1


async def main():
    bot = Bot(token='7688339457:AAGOjOS9j-YT9TSrl3OornjoeG8TCeOIc_8')
    dp = Dispatcher()
    dp.include_router(router1)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye Bye')