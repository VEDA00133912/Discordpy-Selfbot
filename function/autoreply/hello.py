async def hello_reply(message, prefix):
    if message.content.startswith(prefix + 'hello'):
        await message.reply('Hello!', mention_author=False)
        await message.add_reaction('🌞')
