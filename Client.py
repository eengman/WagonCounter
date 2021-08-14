""" This module serves as the launch pad for the bots connection and functionality """
import Connection
import BotEvents
import BotCommands
import WagonOutputDisplay

# Establishes the connection between the bot and discord
established_connection = Connection.on_ready()

# Initializes the bot events to start
start_events = BotEvents.on_ready()

# Initializes the bot commands to start
start_commands = BotCommands

embed = WagonOutputDisplay

