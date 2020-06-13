import aiohttp
import logging
import os
from discord.ext import commands
from dotenv import load_dotenv

# load token and prefix from .env file
load_dotenv()

# set up logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter(('%(asctime)s:%(levelname)s:%(name)s: '
                                        '%(message)s')))
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
cogs = ['cogs.utility', 'cogs.wholesome']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    for cog in cogs:
        bot.load_extension(cog)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        # Compliment the user
        compliment_api = "https://complimentr.com/api"
        async with aiohttp.ClientSession() as session:
            async with session.get(compliment_api) as r:
                if r.status == 200:
                    js = await r.json()
                    compliment = js['compliment']

                    await message.channel.send(
                        f'{message.author.mention} {compliment}'
                    )
        return

    await bot.process_commands(message)

# Log in the bot
bot.run(os.getenv('WHOLESOME_TOKEN'), bot=True, reconnect=True)
