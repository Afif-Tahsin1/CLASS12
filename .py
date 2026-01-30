import discord
from discord.ext import commands
from discord import app_commands
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=["!", "?", "!", "."], intents=intents)
@bot.event
def on_ready():
    print('IDK')
