import discord
from discord.ext import commands
from discord import app_commands
import random


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='help', description="Display all of Eve's Commands")
    async def help(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="Help",
            description="""
                
            
            
            
            """
        )


        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
