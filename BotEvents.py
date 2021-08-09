""" Simple program for the bot to return information about the guild """
import os
import datetime as dt
import discord
from discord import channel
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Discord.py Intents
intents = discord.Intents.default()  # Turns on the connection
intents.members = True  # Ensures the member list will be updated properly
client = discord.Client(intents=intents)  # captures the connection to discord

# Declaration of Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')
TESTING_CHANNEL = os.getenv('TESTING_CHANNEL')

guild_key = client.get_guild(int(TESTING_GUILD_KEY))

# Declaration of Empty Dictionary
list_of_members = []


@client.event
async def on_message(message):
    """ Defines events for which the bot will return information by the user typing commands """
    all_members = get_all_members()  # has all the members visible to the bot

    # returns the number of members in the guild
    if message.content.find("!userCount") != -1:
        await message.channel.send(f"""We currently have {guild_key.member_count} members in our server""")
    elif message.content.startswith('!member'):
        # sends a current member list to the guild channel the bot was called from
        await message.channel.send(f"""The current member list is: """)

        # logic for printing out each member of the guild
        for each_element in range(len(all_members)):
            await message.channel.send(f"""- {all_members[int(each_element)]}""")


@client.event
async def keyword(ctx, word):
    channel = client.get_channel(int(TESTING_CHANNEL))
    messages = await ctx.channel.history(limit=200).flatten()
    count = 0

    for msg in messages:
        if word in msg.content:
            count += 1
            print(count)


def get_all_members():
    """ Returns A list of users currently in the server """
    for each_guild in client.guilds:
        for each_member in each_guild.members:
            temp_storage = each_member  # stores an element of member through each iteration before storing
            list_of_members.append(temp_storage)  # adds the member
    return list_of_members


async def phrase(ctx, days: int = None):
    if days:
        after_date = dt.datetime.utcnow()-dt.timedelta(days=days)
        # limit can be changed to None but that this would make it a slow operation.
        messages = await ctx.channel.history(limit=10, oldest_first=True, after=after_date).flatten()
        print(messages)
    else:
        await ctx.send("please enter the number of days wanted")


client.run(TOKEN)
