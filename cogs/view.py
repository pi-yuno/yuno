import discord
import random

class TTToe(discord.ui.View):
    def bot_move(self):
        av_move = [button for button in self.children if button.label == "\u200b"]
        if av_move:
            bot_choice = random.choice(av_move)
            bot_choice.label = "🇴"
            return True
        return False

    @discord.ui.button(label="\u200b", row=0, style=discord.ButtonStyle.secondary)
    async def one(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=0, style=discord.ButtonStyle.secondary)
    async def two(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=0, style=discord.ButtonStyle.secondary)
    async def threw(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=1, style=discord.ButtonStyle.secondary)
    async def four(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=1, style=discord.ButtonStyle.secondary)
    async def five(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=1, style=discord.ButtonStyle.secondary)
    async def six(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=2, style=discord.ButtonStyle.secondary)
    async def seven(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=2, style=discord.ButtonStyle.secondary)
    async def eight(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)

    @discord.ui.button(label="\u200b", row=2, style=discord.ButtonStyle.secondary)
    async def nine(self, interaction, button):
        button.label = "🇽"
        if self.bot_move():
            await interaction.response.edit_message(view=self)
        else:
            await interaction.response.edit_message(content="`[Game Over!]`", view=None)
