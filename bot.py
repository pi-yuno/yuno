from cogs import command, headers
from cogs.message import _message
from cogs.message_edit import _message_edit
from cogs.reaction import _reaction_add

bot = command.bot

@bot.event
async def on_message(message):
    await _message(message)
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    await _message_edit(before, after)
    await bot.process_commands(after)

@bot.event
async def on_reaction_add(reaction, user):
    await _reaction_add(reaction, user)

bot.run(headers.YUNO)
