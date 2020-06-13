from discord.ext import commands
from datetime import datetime as dt


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

        # Edit the ping message with the round trip time on completion
        await msg.edit(content=f"""
        Pong!\nOne message round-trip took {(dt.timestamp(dt.now()) - start) * 1000} ms
        """)


def setup(bot):
    bot.add_cog(Utility(bot))
