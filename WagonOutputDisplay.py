""" A module which creates an embed for the bots messages """

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Encapsulated Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Declaration Discord.py Variables
client = commands.Bot(command_prefix='!')


@client.command()
async def embed(ctx):
    embed = discord.Embed(title="Top Occurrences of 'Wagon'", description="testing \n testing 2", color=0xFF5733)
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    pass


client.run(BOT_TOKEN)
