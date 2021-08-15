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
bot = commands.Bot(command_prefix='!', intents=intents)  # Declares command prefix for how the bot is called

# Declaration of Discord.py Variables
user_vs_occurrence = {}  # creates an empty dictionary , populated by on_ready()


@bot.event
async def on_ready():
    """
    Initializes the dictionary with all users in the guild once connected and sets
    each members phrase occurrence to 0
    :return: a dictionary of each member(k) of the guild along with an occurrence(v)
    """
    list_of_all_members = get_all_members()
    initial_occurrence = 0

    # Puts each member in a dictionary and gives them a phrase occurrence equal to 0
    for each_member in list_of_all_members:
        user_vs_occurrence[str(each_member)] = initial_occurrence


def update_occurrences(member):
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
    Helper function which returns a list of users currently in the server
    :return: a complete list of all members in the guild
    """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    # TODO - can this be faster than O(n^2)
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
        pass  # do nothing, they are already in the dictionary being recorded
    else:
        user_vs_occurrence[str(member)] = 0  # adds them to the dictionary


@bot.event
async def on_message(message):
    """
    Keeps track of a total talley of how many times 'bhwagon' has been said
    :param message: the message that was sent
    :return: a total amount of times 'bhwagon' has been said in the channel the bots called to
    """
    if "wagon" in message.content:
        update_occurrences(message.author)  # Total sum talley starts at bot launch
        print(user_vs_occurrence)


bot.run(BOT_TOKEN)
