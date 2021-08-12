# TODO - Should the Encapsulated Variables state be in a class of its own ??

import os
import discord
from discord import Guild
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Discord.py Variables
client = discord.Client()  # captures the connection to discord
the_bot = client.user
list_of_guids = client.guilds

# Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')

PRIMARY_GUILD_NAME = os.getenv('PRIMARY_GUILD_NAME')
PRIMARY_GUILD_KEY = os.getenv('PRIMARY_GUILD_KEY')

TESTING_GUILD_NAME = os.getenv('TESTING_GUILD_NAME')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')

WAGON_STEAL_CHANNEL_KEY = os.getenv('WAGON_STEAL_CHANNEL_KEY')

client = discord.Client(intents=intents)
