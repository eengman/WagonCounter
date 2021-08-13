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

bot = commands.Bot(command_prefix='!', intents=intents)  # Declares command prefix

# Declaration of Discord.py Variables
guild_key = bot.get_guild(int(TESTING_GUILD_KEY))


@bot.event
async def on_message(message):
    """ Defines events for which the bot will return information by the user typing commands """
    all_members = get_all_members()  # has all the members visible to the bot

    # Sends to the channel the event is called, the total amount of users in the guild
    if message.content.find("!userCount") != -1:
        await message.channel.send(f"""We currently have {len(all_members)} members in the server""")
    # Sends to the channel the event is called, a list of users currently in the guild
    elif message.content.startswith('!member'):
        await message.channel.send(f"""The current member list is: \n""")
        for each_member in all_members:
            await message.channel.send(f"""- {each_member}""")
            print("Test 0 - ", each_member)
    # elif "wagon" in message.content:
    #     create_dict(message.author)


def get_all_members():
    """ Returns A list of users currently in the server """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in bot.guilds:
        for each_member in each_guild.members:
            list_of_members.append(each_member)  # adds the member
            print("Test 1 - ", list_of_members)
    return list_of_members


@bot.command()
async def find(ctx, days: int = None, *, phrase:str = "wagon"):
    if not (days or phrase):
        return await ctx.send("Please enter a phrase and days")

    after_date = dt.datetime.utcnow()-dt.timedelta(days=days)
    # limit can be changed to None but that this would make it a slow operation.
    messages = await ctx.channel.history(limit=10, oldest_first=True, after=after_date).flatten()
    # loop each message to check for phrase
    for message in messages:
        if phrase in message.content:
            print(message)
        else:
            await ctx.send("please enter the number of days wanted")


bot.run(TOKEN)
