import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


class ChristmasCountdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='christmas-countdown', description="Displays a countdown timer for Christmas")
    async def christmas_timer(self, interaction: discord.Interaction):
        # Get the current date and Christmas date
        current_date = datetime.now()
        christmas_date = datetime(current_date.year, 12, 25)

        # Calculate the remaining time until Christmas
        if current_date > christmas_date:
            # Christmas has passed for this year, calculate for the next year
            christmas_date = datetime(current_date.year + 1, 12, 25)

        time_remaining = christmas_date - current_date
        days_remaining = time_remaining.days
        hours_remaining, remainder = divmod(time_remaining.seconds, 3600)
        minutes_remaining = remainder // 60

        # Create an embed
        embed = discord.Embed(
            title='🎄 Christmas Countdown 🎄',
            description=f'{days_remaining} days, {hours_remaining} hours, '
                        f'and {minutes_remaining} minutes until Christmas!',
            color=0xff0000  # You can set the color of the embed here
        )
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/744639508880031775/1183065568446775357/szabo-viktor-HRcpw5H01Lc-unsplash.jpg?ex=6586faab&is=657485ab&hm=e2ad4da7eba12aeaa50898ac2217c1bf01f8bfc6f07e67bc6bd01a4fb8c45182&'
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(ChristmasCountdown(bot))
