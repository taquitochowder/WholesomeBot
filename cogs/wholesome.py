from discord.ext import commands
import aiohttp
import discord
import io
import requests


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

        # get JSON response from api
        r = requests.get(dog_api)
        if r.status_code != 200:
            return await ctx.send(failure_message)

        # send the dog image
        dog_url = r.json()['message']
        async with aiohttp.ClientSession() as session:
            async with session.get(dog_url) as resp:
                if resp.status != 200:
                    return await ctx.send(failure_message)
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'doggo.jpg'))


def setup(bot):
    bot.add_cog(Wholesome(bot))
