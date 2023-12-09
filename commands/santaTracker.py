import discord
from discord.ext import commands
from discord import app_commands
import random


class SantaTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='santa-tracker', description="Track Santa's last known location")
    async def santatracker(self, interaction: discord.Interaction):

        locations = [
            'the North Pole',
            'a snowy village',
            'a cozy fireplace',
            'a twinkling Christmas tree',
            'a busy toy workshop',
        ]
        last_known_location = random.choice(locations)

        embed = discord.Embed(
            color=0xffcc00,
            title='🎅 Santa Tracker 🎅',
            description=f'Santa was last spotted at {last_known_location}.',
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(SantaTracker(bot))
