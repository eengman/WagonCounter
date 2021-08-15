""" This module serves as the launch pad for the bots connection and functionality """
import Connection
import BotEvents
import EmbededOutputDisplay

# Establishes the connection between the bot and discord
established_connection = Connection.on_ready()

# Handles all the Bot events and returns information about the guild based on event calls
handle_events = BotEvents

# Handles all the bot actions
print_messages = EmbededOutputDisplay



