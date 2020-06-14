from discord.ext import commands
from datetime import datetime as dt
from random import choice


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = dt.timestamp(dt.now())

        msg = await ctx.send(content='Pinging....')

        rtt = (dt.timestamp(dt.now()) - start) * 1000

        # Edit the ping message with the round trip time on completion
        await msg.edit(content=f"""
        Pong!\nOne message round-trip took {rtt} ms
        """)

    @commands.command(
        name='choose',
        description='Randomly choose between given options',
        aliases=['c']
    )
    async def choose_command(self, ctx, *args):
        selected_choice = choice(args)
        await ctx.send(f'{selected_choice} was chosen')


def setup(bot):
    bot.add_cog(Utility(bot))
