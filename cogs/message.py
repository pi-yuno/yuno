import re

async def _message(message):
    # to make convenient
    content = message.content
    author = message.author
    channel = message.channel

    # user specific triggers
    if author.id == 815832253204660244:
        if "https://cdn.discordapp.com/emojis" in content and message.guild.id == 1134568451768320090:
            await channel.purge(limit=1)
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



