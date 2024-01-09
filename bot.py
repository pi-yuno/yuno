import git, os
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

@tasks.loop(minutes=30)
async def update_ai_task():
    try:
        repo = git.Repo('.')
        repo.git.add('myai.json')
        repo.git.commit('-am', 'schedule ai update')
        repo.git.push(f'https://{os.environ["PIYUNO"]}@github.com/pi-yuno/yuno.git', 'master')
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    update_ai_task.start()

bot.run(headers.YUNO)
