import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX', '!') 

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} is Online!')

    async def on_message(self, message):

        if message.content.startswith(PREFIX + 'ping'):
            await message.reply('🏓Pong!', mention_author=False)


client = MyClient()
client.run(TOKEN)