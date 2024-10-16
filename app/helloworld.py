import discord
from discord.ext import commands


class HelloWorldCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.slash_command(description='Envia Hello World no chat.')
    async def helloworld(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello World!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(HelloWorldCommand(bot))
