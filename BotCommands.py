import os
import discord
import datetime as dt
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
user_vs_occurrence = {}  # creates an empty dictionary


@bot.event
async def on_ready():
    """ creates a dictionary of each visible user in the server when the bot """
    initial_occurrence = 0
    list_of_all_members = get_all_members()

    # puts each member in a dictionary and gives them a phrase occurrence of 0
    for each_member in list_of_all_members:
        user_vs_occurrence[str(each_member)] = initial_occurrence
    print("In method ", user_vs_occurrence)


def get_all_members():
    """ Returns A list of users currently in the server """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in bot.guilds:
        for each_member in each_guild.members:
            list_of_members.append(str(each_member))  # adds the member
    return list_of_members


def update_occurrences(user_vs_occurrence, member):
    """ Creates a dictionary of each visible user in the server """
    occurrence = user_vs_occurrence.get(str(member))

    if str(member) in user_vs_occurrence:
        occurrence = occurrence + 1
        user_vs_occurrence.update({str(member): occurrence})
    print("Updated list - ", user_vs_occurrence)


@bot.command()
async def find(ctx, days: int = None, *, phrase: str = None):
    if not (days or phrase):
        return await ctx.send("Please enter a phrase and days")

    after_date = dt.datetime.utcnow() - dt.timedelta(days=days)

    # limit can be changed to None but that this would make it a slow operation.
    messages = await ctx.channel.history(limit=10, oldest_first=True, after=after_date).flatten()

    # loop each message to check for phrase
    for each_message in messages:
        if phrase in each_message.content:
            pass # todo


@bot.command()
async def get_members(ctx):
    member_list = ''

bot.run(TOKEN)
