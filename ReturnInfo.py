""" Simple program for the bot to return information about the guild """
import os
import discord
import time
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file
client = discord.Client()

# Declaration of Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')


@client.event
async def on_message(message):
    """ When a user types !users the bot will return the amount of users in the server """
    guild_key = client.get_guild(int(TESTING_GUILD_KEY))

    if message.content.find("!userCount") != -1:
        await message.channel.send(f"""We currently have {guild_key.member_count} members in our server""")


async def update_info():
    """ Updates specific information and uploads it to a .txt file when called """
    await client.wait_until_ready()
    global messages, target_phrase

client.run(TOKEN)
