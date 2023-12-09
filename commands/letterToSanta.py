import discord
from discord.ext import commands
from discord import app_commands


class LetterToSanta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='letter-to-santa', description="Write a letter to Santa!")
    async def write_santa(self, interaction: discord.Interaction, letter: str):
        embed = discord.Embed(
            title="Your letter has been delivered to the North Pole ✉",
            color=discord.Color.red()
        )
        embed.set_image(url='https://images.unsplash.com/photo-1482386383748-b78a9840bec9?q=80&w=1481&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(LetterToSanta(bot))
