import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
from os import environ
import random
import asyncio

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


async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)



asyncio.run(main())
