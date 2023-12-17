import discord
from cogs import headers

bot = headers.bot

@bot.tree.command(name="sync", description="tree sync")
async def sync(interaction):
    await interaction.response.send_message("done...!")

@bot.tree.command(name="avatar", description="get user avatar image")
async def avatar(interaction, user: discord.Member):
    embed = discord.Embed(description=user.name, color=0xfeadc3)
    embed.set_image(url=user.avatar)
    await interaction.response.send_message(embed=embed)
