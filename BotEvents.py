""" Simple program for the bot to return information about the guild """
import os
import datetime as dt
import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')
TESTING_CHANNEL = os.getenv('TESTING_CHANNEL')

# Declaration of Discord.py Intents
intents = discord.Intents.default()  # Turns on the connection
intents.members = True  # Ensures the member list will be updated properly
client = discord.Client(intents=intents)  # captures the connection to discord

# Declaration of Discord.py Variables
guild_key = client.get_guild(int(TESTING_GUILD_KEY))
bot = commands.Bot(command_prefix='!')


@client.event
async def on_message(message):
    """ Defines events for which the bot will return information by the user typing commands """
    all_members = get_all_members()  # has all the members visible to the bot
    the_count = 0
    create_dict(all_members)

    # Sends to the channel the event is called, the total amount of users in the guild
    if message.content.find("!userCount") != -1:
        await message.channel.send(f"""We currently have {len(all_members)} members in the server""")
    # Sends to the channel the event is called, a list of users currently in the guild
    elif message.content.startswith('!member'):
        await message.channel.send(f"""The current member list is: \n""")
        for each_member in all_members:
            await message.channel.send(f"""- {each_member}""")
    elif "wagon" in message.content:
        create_dict(message.author)


def get_all_members():
    """ Returns A list of users currently in the server """
    list_of_members = []  # Declaration of Empty Dictionary

    # Declaration of logic to print out each user in the guild
    for each_guild in client.guilds:
        for each_member in each_guild.members:
            list_of_members.append(each_member)  # adds the member
    return list_of_members


# @client.event
# async def keyword(ctx, word):
#     channel = client.get_channel(int(TESTING_CHANNEL))
#     messages = await ctx.channel.history(limit=200).flatten()
#     count = 0
#
#     for msg in messages:
#         if word in msg.content:
#             count += 1
#             print(count)


# TODO - get this to work
def create_dict(member):
    """ Creates a dictionary with all the current members of the guild inside """
    player_vs_occurrence = {}  # empty dictionary
    initial_value = 0
    counter = 0

    # Initializes all members in dictionary
    if member != player_vs_occurrence.keys():
        player_vs_occurrence[str(member)] = initial_value
    else:
        player_vs_occurrence[str(member)] = player_vs_occurrence.get(str(member), initial_value+1)

    print(player_vs_occurrence)


client.run(TOKEN)
