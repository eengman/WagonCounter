""" A module which creates an embed for the bots messages """
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

# Declaration of Encapsulated Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Declaration Discord.py Variables
intents = discord.Intents.default()  # Turns on the connection
intents.members = True  # Ensures the member list will be updated properly
client = commands.Bot(command_prefix='!', intents=intents)  # Declares command prefix and turns on all intents

# Declaration of Discord.py Variables
user_vs_occurrence = {}  # creates an empty dictionary , populated by on_ready


@client.event
async def on_ready():
    """ Creates a dictionary of each visible user in the server when the bot initially connects """
    list_of_all_members = get_all_members()
    initial_occurrence = 0

    # puts each member in a dictionary and gives them a phrase occurrence equal to 0
    for each_member in list_of_all_members:
        user_vs_occurrence[str(each_member)] = initial_occurrence


@client.command()
async def wagonSteals(ctx):
    """
    Returns a embeded message from the bot about the top users who've said 'bhwagon'
    :param ctx: context of the command
    :return: a formatted list of users w/ the number of occurrences of 'bhwagon' said
    """
    wagonSteals = discord.Embed(
        title="Wagon Steals Counter",
        url="https://docs.google.com/spreadsheets/d/1or_UMRcmDrRPi1DyxbF0yYWOs7ujeW0qTmsf6nwrqPc/edit#gid=1230983397",
        description=" text ",
        color=0x2AB050)

    # This shows the member who called the bot function
    wagonSteals.set_author(name=ctx.author.display_name,
                       url="https://www.blackhatsride.com",
                       icon_url=ctx.author.avatar_url)
    await ctx.send(embed=wagonSteals)


@client.command()
async def members(ctx):
    """
    Returns a complete list of the members when a member of the guild types !members
    along with the total number of users, including breaking the number of users down by roles
    :param ctx: context of the command
    :return: a complete list of members, the total amount in each role
    """
    all_members = get_all_members()

    # TODO - replace over the testing roles
    # black_hats = ctx.guild.get_role(813926082960162866)
    # prospectors = ctx.guild.get_role(822261499384037418)
    # prospects = ctx.guild.get_role(861013512189116446)
    # recruits = ctx.guild.get_role(813925577383084052)

    # testing roles - TODO - delete after testing
    purple = ctx.guild.get_role(876356417085374485)
    green = ctx.guild.get_role(876356464632025110)

    members = discord.Embed(
        title="Current Members List",
        url="https://www.blackhatsride.com/about-us",
        description='-' + "\n-".join(all_members),
        color=0x4EEDEB)

    # This shows the member who called the bot function
    members.set_author(name=ctx.author.display_name,
                       url="https://www.blackhatsride.com",
                       icon_url=ctx.author.avatar_url)

    # members.add_field(name="Current member count is ".title(), value=str(len(all_members)), inline=False)
    # members.add_field(name="Current Black Hat count is ".title(), value=str(len(black_hats)), inline=False)
    # members.add_field(name="Current Prospectors count is ".title(), value=str(len(prospectors)), inline=False)
    # members.add_field(name="Current Prospects count is ".title(), value=str(len(prospects)), inline=False)
    # members.add_field(name="Current Recruits count is ".title(), value=str(len(recruits)), inline=False)

    members.add_field(name="Current member count is ".title(), value=str(len(all_members)), inline=False)
    members.add_field(name="Total Amount of Purple Roles ".title(), value=str(len(purple.members)), inline=False)
    members.add_field(name="Total Amount of Green Roles ".title(), value=str(len(green.members)), inline=False)
    # TODO - add one more field and replace with the correct name and value above
    await ctx.send(embed=members)


@client.command()
async def guide(ctx):
    """
    returns a Survival Guide - Outlaw 101, created by a member of the Black Hats
    :param ctx: context
    :return: a hyperlink to a website which contains the survival guide - outlaw 101
    """
    guide = discord.Embed(
        title="Black Hat RDO Guide - Outlaw 101",
        url="https://docs.google.com/spreadsheets/d/1or_UMRcmDrRPi1DyxbF0yYWOs7ujeW0qTmsf6nwrqPc/edit#gid=1230983397",
        description="This is the RDO Black Hats Guide, which will be helpful for new and veteran players alike. Feel "
                    "free to download a copy and use it as you wish!",
        color=0xE39DC2)

    # This shows the member who called the bot function
    guide.set_author(
        name="Katykinss#8895",
        url="https://www.twitch.tv/katymcblagg",
        icon_url="https://pbs.twimg.com/profile_images/1373717181276491780/vOus29er_400x400.jpg")
    await ctx.send(embed=guide)


@client.command()
async def eliteRanks(ctx):
    """
    Returns a list of possible roles the member may earn
    :param ctx: context of the discord bot
    :return: a complete list of all possible roles the members may earn
    """
    eliteRanks = discord.Embed(
        title="Black Hat RDO - Elite Titles",
        url="https://docs.google.com/spreadsheets/d/1or_UMRcmDrRPi1DyxbF0yYWOs7ujeW0qTmsf6nwrqPc/edit#gid=1230983397",
        description="This is a list of the 'Elite Titles' that can be earned as described below ",
        color=0xFFDF00)

    # This shows the member who called the bot function
    eliteRanks.set_author(name=ctx.author.display_name,
                          url="https://www.blackhatsride.com",
                          icon_url=ctx.author.avatar_url)

    eliteRanks.add_field(name="The Honorable".title(), value="Given monthly to whichever Black Hat has accrued the most"
                                                             " honor points for the month.", inline=False)
    eliteRanks.add_field(name="Wagon Whisperer".title(), value="Given Monthly to whichever Black Hat steals the most "
                                                               "wagons in the month.", inline=False)
    eliteRanks.add_field(name="Wagon Chief".title(), value="This title, once earned stays with you. To earn this Elite "
                                                           "Title, you must complete the following challenges: \n- Be a"
                                                           " Full Black Hat. (Cannot be a recruit or prospect.) \n- 50 "
                                                           "Wagons stolen as the Posse leader and documented in the "
                                                           "Wagon Steal Counter channel. \n- Stolen a Wagon without "
                                                           "killing anyone (Must be witnessed by at least two Black Hat"
                                                           "s) \n- Stolen a Wagon solo. (Must be witnessed by at least "
                                                           "two Black Hats. You may still posse up and announce the "
                                                           "steal as usual, but the posse will remain in Valentine "
                                                           "while the player pursuing the challenge completes the steal."
                                                           ")"
                         , inline=False)
    eliteRanks.set_footer(text="Notes: a single witness may be substituted for a video and/or stream")
    await ctx.send(embed=eliteRanks)


@client.command()
async def commands(ctx):
    """
    A message from the bot containing all of the commands that may be used
    :param ctx: context of the bot command
    :return: returns a message from the bot that has all the commands and their descriptions
    """
    commands = discord.Embed(
        title="WagonCounter Command Help",
        description="Here is a list of the different bot commands that you may use to call on me!",
        color=0xF70C1C)

    # This shows the member who called the bot function
    commands.set_author(name=ctx.author.display_name,
                        url="https://www.blackhatsride.com",
                        icon_url=ctx.author.avatar_url)

    commands.add_field(name="!wagonSteal xx", value="Returns a list of users along with the occurrences of how often "
                                                    "they have said 'bhwagon' in the server", inline=False)
    commands.add_field(name="!members", value="Returns a list of each member in the guild, along with how many of each "
                                              "role, and then a total count of members.", inline=False)
    commands.add_field(name="!guide", value="Returns a link to the Black Hat Out Law 101 - Survival Guide created by "
                                            "Katykinss#8895.", inline=False)
    commands.add_field(name="!eliteRanks", value="Returns all the additional titles members may earn", inline=False)

    await ctx.send(embed=commands)


def get_all_members():
    """ Returns A list of users currently in the server """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in client.guilds:
        for each_member in each_guild.members:
            list_of_members.append(str(each_member))  # adds the member
    return list_of_members


client.run(BOT_TOKEN)
