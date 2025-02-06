from function.autoreply import hello_reply, bye_reply
from function.commands import about_reply, perm_reply, ping_reply

async def on_message_handler(message, prefix):
    await ping_reply(message, prefix)
    await hello_reply(message, prefix)
    await bye_reply(message, prefix)
    await perm_reply(message, prefix)
    await about_reply(message, prefix)
