import os
import discord
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration Discord.py Variables
client = discord.Client()  # captures the connection to discord

# Encapsulated Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
PRIMARY_GUILD_NAME = os.getenv('PRIMARY_GUILD_NAME')
PRIMARY_GUILD_KEY = os.getenv('PRIMARY_GUILD_KEY')
TESTING_GUILD_NAME = os.getenv('TESTING_GUILD_NAME')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')
WAGON_STEAL_CHANNEL_KEY = os.getenv('WAGON_STEAL_CHANNEL_KEY')


@client.event
async def on_ready():
    """ Confirms the bot has successfully connected to the targeted server """
    for each_guild in client.guilds:
        if each_guild.name == PRIMARY_GUILD_NAME:
            print("Locked In 😎\n")  # we are where we want to be
        elif each_guild.name == TESTING_GUILD_NAME:
            print(f"{client.user} is connected to {each_guild.name}, which is recognized as a Testing "
                  f"Guild\n")
        else:
            print("Name's didn't match 🤔")
        print(f'{client.user} has successfully connected to {each_guild.name}! 😁\n')


def get_all_members():
    """ Returns A list of users currently in the server """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in client.guilds:
        for each_member in each_guild.members:
            list_of_members.append(str(each_member))  # adds the member
    return list_of_members


def populate_dictionary():
    """ creates a dictionary of each visible user in the server """
    user_vs_occurrence = {}  # creates an empty dictionary
    list_of_all_members = get_all_members()

    # puts each member in a dictionary and gives them a phrase occurrence of 0
    for each_member in list_of_all_members:
        user_vs_occurrence[str(each_member)] = 0
    return user_vs_occurrence


client.run(BOT_TOKEN)
