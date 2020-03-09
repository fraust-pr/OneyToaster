import discord
import random
from discord.ext import commands

class PUTEMUP(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def d20(self, ctx):
        d20 = random.randint(1, 20)
        await ctx.channel.send(d20)

    @commands.command()
    async def d12(self, ctx):
        d12 = random.randint(1, 12)
        await ctx.channel.send(d12)

    @commands.command()
    async def d10(self, ctx):
        d10 = random.randint(1, 10)
        await ctx.channel.send(d10)

    @commands.command()
    async def d8(self, ctx):
        d8 = random.randint(1, 8)
        await ctx.channel.send(d8)

    @commands.command()
    async def d6(self, ctx):
        d6 = random.randint(1, 6)
        await ctx.channel.send(d6)

    @commands.command()
    async def d4(self, ctx):
        d4 = random.randint(1, 4)
        await ctx.channel.send(d4)
    


def setup(client):
    client.add_cog(PUTEMUP(client))