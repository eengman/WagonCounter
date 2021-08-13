# TODO - Should the Encapsulated Variables state be in a class of its own ??
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


@bot.command("wagon")  # added
async def find(ctx, days: int = None, *, phrase: str = None):
    if not (days or phrase):
        return await ctx.send("Please enter a phrase and days")

    after_date = dt.datetime.utcnow() - dt.timedelta(days=days)
    # limit can be changed to None but that this would make it a slow operation.
    messages = await ctx.channel.history(limit=10, oldest_first=True, after=after_date).flatten()
    # loop each message to check for phrase
    for message in messages:
        if phrase in message.content:
            print(message)
        else:
            await ctx.send("please enter the number of days wanted")


@bot.command()
async def get_members(ctx):
    member_list = ''


for member in ctx.message.server.members:
    member_list += member.name
print(member_list)
