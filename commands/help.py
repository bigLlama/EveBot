import discord
from discord.ext import commands
from discord.ext.commands import CommandError
from discord import app_commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='help', description="Display all of Eve's Commands")
    async def help(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="Hi, I'm Eve...Christmas Eve ⛄",
            description="""
            **Basic Commands**
            `/christmas-countdown: `Display the countdown until Christmas
            `/letter-to-santa: `Send a letter to Santa
            `/mistletoe: `A mistletoe will appear above two lucky users
            `/santa-tracker` Track Santa's last known location\n
            **Gifts**
            `/gift @user: `Send a virtual gift to a user
            `/top-received` Show the top 10 users with the most gifts received in the server
            `/top-sent` Show the top 10 users with the most gifts sent in the server
            
            """,
            color=0x3498db  # You can set the color to whatever you prefer
        )


        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
