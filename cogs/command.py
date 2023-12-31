import os
import json
import random
import discord
import requests
import asyncio
from cogs import application, headers
from discord.ext import commands
from cogs.brick import Display, Ball
from cogs.view import TTToe

bot = application.bot


@bot.command()
async def ttt(ctx):
    await ctx.send(view=TTToe())

@bot.command()
async def sleep(ctx):
    if ctx.author.id == 1098141251209023538:
        os.remove("TRUE")
        await bot.close()

@bot.command()
@commands.is_owner()
async def logai(ctx):
    with open("myai.json") as file:
        data = json.load(file)
    await ctx.send(str(data))

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=int(limit + 1))
    await ctx.message.delete()

@purge.error
async def purge_err(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("not allowed!")

global _ball_mode
_ball_mode = dict()
async def _ball(ctx):
    message = await ctx.send("Starting....")
    ball = Ball(15, 27)
    display = Display(16, 28)
    while _ball_mode[ctx.author]:
        x, y = ball.play()
        display.clear()
        display.draw(x, y)
        await message.edit(content=str(f"```\n{display.render()}\n```"))
        await asyncio.sleep(0.5)
    await message.edit(content="`[ Game Over! ]`")

@bot.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx, channel:discord.TextChannel, seconds: int):
    await channel.edit(slowmode_delay=seconds)
    await ctx.reply(f"Slowmode in {channel} is set to {seconds} seconds")

@bot.command()
@commands.has_permissions(administrator=True)
async def annoy(ctx, user:discord.Member):
    while True:
        await user.send("cocksucker..")
        await ctx.reply(f"annoying {user.mention}")
@bot.command()
async def ballz(ctx, arg = None):
    global _ball_mode
    if arg == "auth":
        _list = "players: "
        for user, mode in _ball_mode.items():
            if mode:
                _list += f"`{user.name}`\t"
            else:
                _list += f"{user.name}\t"
        await ctx.reply(_list)
        return
    if arg == "off":
        if ctx.author in _ball_mode and _ball_mode[ctx.author]:
            _ball_mode[ctx.author] = False
            return
        else:
            await ctx.reply("no games running by you!")
            return
    _ball_mode[ctx.author] = True
    await _ball(ctx)

@bot.command()
async def update(ctx):
    await bot.close()

@bot.command()
async def react(ctx, *args):
    reactions = headers.reactions
    if len(args) == 0:
        reaction = random.choice(reactions)
        embed = discord.Embed(title=None,description=reaction,color=0xfeadc3)
        data = requests.get(f"https://api.otakugifs.xyz/gif?reaction={reaction}").json()
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
        return
    if args[0] in reactions:
        embed = discord.Embed(title=None,description=args[0],colour=0xfeadc3)
        data = requests.get(f"https://api.otakugifs.xyz/gif?reaction={args[0]}").json()
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
        return
    if args[0] in ["h", "help"]:
        reactions_form = '\t'.join(reactions)
        embed = discord.Embed(title="Reactions",description=reactions_form,color=0xfeadc3)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
        await ctx.reply(embed=embed)
        return
    await ctx.reply(f"`ERROR: No reactions found {args[0]}`\ntry\t`h|help`")
