""" This module handles the connection between the bot and Discord """

import os
import discord
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration Discord.py Variables
client = discord.Client()  # captures the connection to discord

# Encapsulated Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
PRIMARY_GUILD_NAME = os.getenv('PRIMARY_GUILD_NAME')
TESTING_GUILD_NAME = os.getenv('TESTING_GUILD_NAME')


@client.event
async def on_ready():
    """
     Confirms the bot has successfully connected to the targeted server along with setting the game activity
    :return: Prints a message to console letting know where the bot connected
    """
    for each_guild in client.guilds:
        if each_guild.name == PRIMARY_GUILD_NAME:
            print("Locked In 😎\n")  # we are where we want to be
        elif each_guild.name == TESTING_GUILD_NAME:
            print(f"{client.user} is connected to {each_guild.name}, which is recognized as a Testing "
                  f"Guild\n")
        else:
            print("Name's didn't match 🤔")
        print(f'{client.user} has successfully connected to {each_guild.name}! 😁\n')
    await client.change_presence(activity=discord.Game('RDO - Wagon Stealing'))  # sets the bots Activity

client.run(BOT_TOKEN)
