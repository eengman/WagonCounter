import os

import discord
from dotenv import load_dotenv

load_dotenv()

# Declaration Discord.py Variables
client = discord.Client()
the_bot = client.user
list_of_guids = client.guilds


# Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')

PRIMARY_GUILD_NAME = os.getenv('PRIMARY_GUILD_NAME')
PRIMARY_GUILD_KEY = os.getenv('PRIMARY_GUILD_KEY')

TESTING_GUILD_NAME = os.getenv('TESTING_GUILD_NAME')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')

WAGON_STEAL_CHANNEL_KEY = os.getenv('WAGON_STEAL_CHANNEL_KEY')

client = discord.Client()


@client.event
async def on_ready():
    """ Confirms the bot has successfully connected to the server we targeted """
    for each_guild in client.guilds:
        if each_guild.name == PRIMARY_GUILD_NAME:
            print("Locked In 😎\n")  # we are where we want to be
        elif each_guild.name == TESTING_GUILD_NAME:
            print(f"This guild is {client.user} is connected to, is recognized as a Testing Guild\n")
        else:
            print("Name's didn't match 🤔")

    print(f'{client.user} has successfully connected to {each_guild.name}! 😁')


client.run(TOKEN)
