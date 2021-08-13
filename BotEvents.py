""" Simple program for the bot to return information about the guild """
import os
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
    elif "wagon" in message.content:
        print("Inital dict - ", populate_dictionary())
        update_occurrences(populate_dictionary(), message.author)


@bot.event
async def on_ready():
    """ Shows that the bot is playing a game """
    await bot.change_presence(activity=discord.Game('RDO - Wagon Stealing'))


def get_all_members():
    """ Returns A list of users currently in the server """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in bot.guilds:
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


def update_occurrences(user_vs_occurrence, member):
    """ creates a dictionary of each visible user in the server """
    occurrence = user_vs_occurrence.get(str(member))

    if str(member) in user_vs_occurrence:
        occurrence = occurrence + 1
        user_vs_occurrence.update({str(member): occurrence})
    print(user_vs_occurrence)


bot.run(TOKEN)
