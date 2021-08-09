""" Simple program to define the bots main functionality """
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import BotEvents as members_c

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Discord.py Variables
client = discord.Client()  # captures the connection to discord

# Declaration of Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')

# Program Variables
target_phrase = "bhwagon".casefold()  # negates differences cases of this phrase
list_of_users = []  # Declares an empty dictionary
guild_key = client.get_guild(int(TESTING_GUILD_KEY))

"""  PROGRAM START  """

""" Get the list of users in this program """

client.run(TOKEN)
