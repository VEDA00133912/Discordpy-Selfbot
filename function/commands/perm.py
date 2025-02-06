import discord

async def perm_reply(message, prefix):
    if message.content.startswith(prefix + 'perm'):
        permissions = message.author.guild_permissions
        perm_list = [perm[0] for perm in permissions if perm[1]]

        if perm_list:
            perm_text = "```\n" + "\n".join(perm_list) + "\n```"
        else:
            perm_text = "```\nNo permissions.\n```"

        await message.reply(perm_text, mention_author=False)