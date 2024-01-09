import re
import discord
from cogs import headers

async def _message(message):
    # to make convenient
    content = message.content
    author = message.author
    channel = message.channel

    # unprefix commands
    if content.lower().startswith("stick"):
        if not author.guild_permissions.add_reactions:
            await message.channel.send("You don't have Permissions to add emotes.")
            return
        await message.delete()
        args = content.split(" ")
        match args[1].lower():
            case "a" | "add":
                if len(args) >= 4:
                    name = args[2]
                    file = headers.downimg(args[3])
                    if not file:
                        embed = discord.Embed(title="Failed",description=f"check url",color=discord.Color.red())
                        await message.channel.send(embed=embed)
                        return
                    embed = discord.Embed(title="Successful",description=f"added sticker {name}.",color=discord.Color.pink())
                    embed.set_thumbnail(url=args[3])
                    await message.guild.create_sticker(name=name, description="None", emoji="🙂", file=discord.File(file))
                    await message.channel.send(embed=embed)

            case "v" | "vanish":
                stickers = message.guild.stickers
                to_del = []
                for sticker in stickers:
                    if sticker.name.lower().startswith(args[2].lower()):
                        to_del.append(sticker)
                if len(to_del) >= 2:
                    embed = discord.Embed(title="Stickers",description=None,color=discord.Color.red())
                    for sticker in to_del:
                        embed.add_field(name=sticker.name, value="\u200b", inline=False)
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="Successful",description=f"removed sticker {to_del[0].name}.",color=discord.Color.pink())
                    await message.channel.send(embed=embed)
                    await message.guild.delete_sticker(to_del[0])

    # user specific triggers
    if author.id == 815832253204660244:
        if "https://cdn.discordapp.com/emojis" in content and message.guild.id == 1134568451768320090:
            await message.delete()
            new = re.sub(r'https://cdn\.discordapp\.com/emojis/\S+', '', content)
            webhook = await channel.create_webhook(name=author.display_name)
            await webhook.send(
                    str(new),
                    username=author.display_name,
                    avatar_url=author.avatar
                    )
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                await webhook.delete()

