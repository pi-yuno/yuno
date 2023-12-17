import os
from cogs import command, headers
from cogs.message import _message
from cogs.message_edit import _message_edit

bot = command.bot

@bot.event
async def on_message(message):
    await _message(message)
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    await _message_edit(before, after)
    await bot.process_commands(after)


bot.run(headers.YUNO)
