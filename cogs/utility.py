from discord.ext import commands
from datetime import datetime as dt
from random import choice, randint


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

    @commands.command(
        name='8ball',
        description='Simulate a magic 8-ball',
        aliases=['8b']
    )
    async def eightball_command(self, ctx):
        responses = {
            1: 'It is certain.',
            2: 'It is decidedly so.',
            3: 'Without a doubt.',
            4: 'Yes – definitely.',
            5: 'You may rely on it.',
            6: 'As I see it, yes.',
            7: 'Most likely.',
            8: 'Outlook good.',
            9: 'Yes.',
            10: 'Signs point to yes.',
            11: 'Reply hazy, try again.',
            12: 'Ask again later.',
            13: 'Better not tell you now.',
            14: 'Cannot predict now.',
            15: 'Concentrate and ask again.',
            16: 'Don\'t count on it.',
            17: 'My reply is no.',
            18: 'My sources say no.',
            19: 'Outlook not so good.',
            20: 'Very doubtful.',
        }

        r = randint(1, 20)

        await ctx.send(responses[r])


def setup(bot):
    bot.add_cog(Utility(bot))
