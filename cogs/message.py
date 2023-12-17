import discord

async def _message(message):
    if message.content == "hi":
        await message.channel.send("hello")
