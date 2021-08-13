""" This client serves as the launch pad for the bots functionality """
import BotEvents as events
import Connection as connection
from Connection import *

# Establishes the connection between the bot and discord
established_connection = connection.on_ready

# Declares the main functionality for the bot
start_events = events.on_message
