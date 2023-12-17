import random
import discord
import requests
from cogs import application
from discord.ext import commands

bot = application.bot

@bot.command()
@commands.is_owner()
async def sleep(ctx):
    await ctx.send("Good night")
    await bot.close()

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=int(limit + 1))
    await ctx.message.delete()

@purge.error
async def purge_err(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("not allowed!")

@bot.command()
async def react(ctx, *args):
    reactions = ['airkiss', 'angrystare', 'bite', 'bleh', 'blush', 'brofist', 'celebrate', 'cheers', 'clap', 'confused', 'cool', 'cry', 'cuddle', 'dance', 'drool', 'evillaugh', 'facepalm', 'handhold', 'happy', 'headbang', 'hug', 'kiss', 'laugh', 'lick', 'love', 'mad', 'nervous', 'no', 'nom', 'nosebleed', 'nuzzle', 'nyah', 'pat', 'peek', 'pinch', 'poke', 'pout', 'punch', 'roll', 'run', 'sad', 'scared', 'shout', 'shrug', 'shy', 'sigh', 'sip', 'slap', 'sleep', 'slowclap', 'smack', 'smile', 'smug', 'sneeze', 'sorry', 'stare', 'stop', 'surprised', 'sweat', 'thumbsup', 'tickle', 'tired', 'wave', 'wink', 'woah', 'yawn', 'yay', 'yes']
    if len(args) == 0:
        reaction = random.choice(reactions)
        embed = discord.Embed(title=None,description=reaction,color=0xfeadc3)
        data = requests.get(f"https://api.otakugifs.xyz/gif?reaction={reaction}").json()
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
        return
    if args[0] in reactions:
        embed = discord.Embed(title=None,description=args[0],colour=0xfeadc3)
        data = await fetch_json(f"https://api.otakugifs.xyz/gif?reaction={args[0]}")
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
        return
    if args[0] in ["h", "help"]:
        reactions_form = '\t'.join(reactions)
        embed = discord.Embed(title="Reactions",description=reactions_form,color=0xfeadc3)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
        await ctx.reply(embed=embed)
        return
    await ctx.reply(f"`ERROR: No reactions found {args[0]}`\ntry\t`?anime h|help` !")
