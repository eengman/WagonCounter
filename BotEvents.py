""" Simple program for the bot to return information about the guild """
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Encapsulated Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')

# Declaration of Discord.py Intents
intents = discord.Intents.default()  # Turns on the connection
intents.members = True  # Ensures the member list will be updated properly
bot = commands.Bot(command_prefix='!', intents=intents)  # Declares command prefix

# Declaration of Discord.py Variables
user_vs_occurrence = {}  # creates an empty dictionary , populated by on_ready


@bot.event
async def on_ready():
    """
    Initializes the dictionary with all users in the guild and sets their occurrence to 0
    :return: a dictionary of each member(k) of the guild along with an occurrence(v)
    """
    list_of_all_members = get_all_members()
    initial_occurrence = 0

    # puts each member in a dictionary and gives them a phrase occurrence equal to 0
    for each_member in list_of_all_members:
        user_vs_occurrence[str(each_member)] = initial_occurrence


def update_occurrences(member):  # took away user occurrence, think it still works
    """
    Updates the users occurrence when 'wagon' is said in a guild channel the bot is connected to
    :param member:
    :return:
    """
    occurrence = user_vs_occurrence.get(str(member))

    if str(member) in user_vs_occurrence:
        occurrence = occurrence + 1
        user_vs_occurrence.update({str(member): occurrence})


def get_all_members():
    """
    Returns A list of users currently in the server
    :return: a complete list of all members
    """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in bot.guilds:
        for each_member in each_guild.members:
            list_of_members.append(str(each_member))  # adds the member
    return list_of_members


@bot.event
async def on_member_join(member):
    """
    Checks to see when a new member join, and if they are in the dictionary or not
    :param member: is the new user who joined the guild
    :return: an updated dictionary with the new member with an occurrence set to 0
    """
    if member in user_vs_occurrence:
        pass
    else:
        user_vs_occurrence[str(member)] = 0


@bot.event
async def on_message(message):
    """
    TODO -
    :param message:
    :return:
    """
    if "wagon" in message.content:
        update_occurrences(message.author)  # Total sum talley starts at bot launch


bot.run(BOT_TOKEN)
