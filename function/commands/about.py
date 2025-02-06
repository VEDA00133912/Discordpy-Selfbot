async def about_reply(message, prefix):
    if message.content.startswith(prefix + 'about'):
        about_text = "```\n" + \
                     f"Name     : {message.guild.me.display_name} ({message.guild.me.id})\n" + \
                     "Library  : discord.py-self\n" + \
                     f"Prefix   : {prefix}\n\n" + \
                     "Commands : about, perm, ping\n" + \
                     "Autoreply: hello, bye\n" + \
                     "Make it a Quote: Mention when replying\n" + \
                     "```"
        
        await message.reply(about_text, mention_author=False)