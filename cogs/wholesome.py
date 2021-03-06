from discord.ext import commands
import aiohttp
import discord
import io


class Wholesome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if (self.bot.user.mentioned_in(message) and
           message.mention_everyone is False):
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

    @commands.command(
        name='doggo',
        description='Sends a random dog image',
        aliases=['dog']
    )
    async def doggo_command(self, ctx):
        failure_message = 'Could not send doggo... :cry:'

        # api endpoint for getting random dog images
        dog_api = 'https://dog.ceo/api/breeds/image/random'

        async with aiohttp.ClientSession() as session:
            async with session.get(dog_api) as r:
                if r.status == 200:
                    js = await r.json()
                    dog_url = js['message']

                    # send the dog image
                    async with session.get(dog_url) as resp:
                        if resp.status != 200:
                            return await ctx.send(failure_message)
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file=discord.File(data, 'doggo.jpg'))
                else:
                    return await ctx.send(failure_message)

    @commands.command(
        name='catto',
        description='Sends a random cat image',
        aliases=['cat']
    )
    async def catto_command(self, ctx):
        failure_message = 'Could not send catto... :cry:'

        # api endpoint for getting random cat images
        cat_api = 'https://cataas.com/cat'

        async with aiohttp.ClientSession() as session:
            async with session.get(cat_api) as r:
                if r.status == 200:
                    data = io.BytesIO(await r.read())
                    await ctx.send(file=discord.File(data, 'catto.jpg'))
                else:
                    return await ctx.send(failure_message)

    @commands.command(
        name='dadjoke',
        description='Sends a dad joke',
        aliases=['dj']
    )
    async def dadjoke_command(self, ctx):
        failure_message = 'Could not send dad joke... :cry:'

        # url to get dad jokes
        joke_api = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'text/plain'}

        async with aiohttp.ClientSession() as session:
            async with session.get(joke_api, headers=headers) as r:
                if r.status == 200:
                    joke = await r.text()
                    await ctx.send(joke)
                else:
                    return await ctx.send(failure_message)


def setup(bot):
    bot.add_cog(Wholesome(bot))
