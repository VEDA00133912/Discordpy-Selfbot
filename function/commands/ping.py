async def ping_reply(message, prefix):
    if message.content.startswith(prefix + 'ping'):
        await message.reply('🏓Pong!', mention_author=False)
