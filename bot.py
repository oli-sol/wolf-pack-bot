"""
Entry point for bot
"""
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

initial_extensions = ["zephyr", "raid", "speech"]

# Here we load our extensions(cogs) listed above in [initial_extensions].
for extension in initial_extensions:
    bot.load_extension("cogs." + extension)

bot.run(TOKEN)
