async def bye_reply(message, prefix):
    if message.content.startswith(prefix + 'bye'):
        await message.reply('Bye!', mention_author=False)
        await message.add_reaction('👋') 
