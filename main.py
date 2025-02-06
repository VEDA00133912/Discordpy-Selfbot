import os
import discord
from dotenv import load_dotenv
from event.on_message.message import on_message_handler  

load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX', '!') 

client = discord.Client() 

@client.event
async def on_ready():
    print(f'{client.user} is Online!')

@client.event
async def on_message(message):
    await on_message_handler(message, PREFIX)

client.run(TOKEN)