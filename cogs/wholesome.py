from discord.ext import commands
import aiohttp
import discord
import io


class Wholesome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='doggo',
        description='Sends a random dog image',
        aliases=['dog']
    )
    async def doggo_command(self, ctx):
        failure_message = 'Could not send dog... :cry:'

        # api endpoint for getting random dog images
        dog_api = 'https://dog.ceo/api/breeds/image/random'

        # get dog image url
        dog_url = None
        async with aiohttp.ClientSession() as session:
            async with session.get(dog_api) as r:
                if r.status == 200:
                    js = await r.json()
                    dog_url = js['message']
                else:
                    return await ctx.send(failure_message)

        # send the dog image
        async with aiohttp.ClientSession() as session:
            async with session.get(dog_url) as resp:
                if resp.status != 200:
                    return await ctx.send(failure_message)
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'doggo.jpg'))


def setup(bot):
    bot.add_cog(Wholesome(bot))
