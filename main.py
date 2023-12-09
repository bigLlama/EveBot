import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord import app_commands
from os import environ
import asyncio
import traceback
import sys

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())
load_dotenv()
TOKEN = environ["TOKEN"]


@bot.event  # Bot is ready
async def on_ready():
    print('Online as {0.user}'.format(bot))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
        print()
    except Exception as e:
        print(e)


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, app_commands.errors.CommandOnCooldown):
        timer = error.retry_after

        if timer >= 3600:
            timer_format = "hours"
            timer = error.retry_after / 3600
        elif timer >= 60:
            timer_format = "min"
            timer = error.retry_after / 60
        else:
            timer_format = "seconds"

        embed = discord.Embed(color=discord.Color.blue())
        embed.set_thumbnail(
            url=interaction.user.avatar)
        embed.add_field(name="Cooldown", value=f"You are on cooldown!\nTry again in `{round(timer)} {timer_format}`")
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)



asyncio.run(main())
