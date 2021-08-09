""" Simple program to define the bots main functionality """
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

"""
Module Scope: 
    Define functionality for which a bot can be called (bhwagon! 7), and goes back into the messages on a specific 
guild channel, and returns the number of occurrences of a defined phrase along with a list of users who said it, ranked 
largest to smallest. 

- where 'bhwagon!' executes a specific action
- 7 represents the amount of days to go back
- phrase = bhwagon

Algorithm to Define

1) define a bot command, which the bot wakes up to when its called  -  ex. !bhwagon 
2) Bot can look back into the message of a specific channel, searching for a specific phrase  -  ex. bhwagon
3) Counts the occurrences of bhwagon, along with which member said each
4) Returns a *score board* of the users with the amount of times said in a specificed number of days

ex. 

* defined call: 
!bhwagon 6 

* returns: 
Eric - 11 times
Tyler - 3 times
Paul - 3 times
Tim - 1 time


    if phrase.author == client.user:
        return  # If the bot said the phrase, we want to skip over it
"""

load_dotenv()  # loads the encapsulated values from the .env file
client = discord.Client()

# Declaration of Encapsulated Variables
TOKEN = os.getenv('BOT_TOKEN')
TESTING_GUILD_KEY = os.getenv('TESTING_GUILD_KEY')

# Program Variables
target_phrase = "bhwagon".casefold()


client.run(TOKEN)
