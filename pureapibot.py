import os
from dotenv import load_dotenv
import asyncio
import telegram

load_dotenv()


async def main():
    bot = telegram.Bot(os.getenv('TOKEN'))
    async with bot:
        print('My INFO: ', await bot.get_me())
        updates = (await bot.get_updates())[0]
        print(updates)
        await bot.send_message(text='Hi John!', chat_id=1234567890)


if __name__ == '__main__':
    asyncio.run(main())
