import os
from discord.ext import tasks
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

@tasks.loop(seconds=5)
async def update_ai_task():
    try:
        # os.system("git add myai.json")
        # os.system("git commit -am  scheduleai")
        # os.system("git push https://$GH_TOKEN@github.com/pi-yuno/yuno.git master")
        await bot.close()
    except:
        pass

@bot.event
async def on_ready():
    os.system("git config --global user.name hakureii")
    os.system("git config --global user.email hakureii@asia.com")
    update_ai_task.start()

bot.run(headers.YUNO)
