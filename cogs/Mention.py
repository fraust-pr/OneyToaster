import discord
from discord.ext import commands

class Mention(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member(self, member):
        victim = member.Mention
        await self.client.get_channel.send(f"{victim} IS HERE TO GET HIS ASS KICKED")
        print(f'{member} IS HERE TO GET HIS ASS KICKED')

def setup(client):
    client.add_cog(Mention(client))