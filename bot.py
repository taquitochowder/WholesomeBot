import logging
import os
from discord.ext import commands
from dotenv import load_dotenv

# load token and prefix from .env file
load_dotenv()

# set up logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


def get_prefix(client, message):
    """Function to pass to bot initializer for dynamic prefixes.
    """

    prefix = os.getenv('WHOLESOME_PREFIX')

    if not message.guild:
        # no prefix necessary in DMs
        prefix = ''

    return prefix


bot = commands.Bot(
    command_prefix=get_prefix,
    description='A bot that promots wholesomeness',
    owner_id=116574449343528962,
    case_insensitive=True
)

# get command groups (cogs)
cogs = ['cogs.utility']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)

# Log in the bot
bot.run(os.getenv('WHOLESOME_TOKEN'), bot=True, reconnect=True)
