import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot(command_prefix = 'rb!')
class Jayden(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Jayden machine is loaded.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 854156802325479434:
            return
        elif 'ur mom' in message.content:
            await message.channel.send('Actually came back from buying cigarettes.')
        elif 'Wiccan' in message.content:
            await message.channel.send('Wiccan is inferior to I')
        elif 'funsies' in message.content:
            await message.channel.send('Are you just trying to ruin Reubens life?')
        elif 'dead chat' in message.content:
            await message.channel.send('Only dead because we are hiding from you.')
        elif 'Ur mom' in message.content:
            await message.channel.send('Actually came back from buying cigarettes.')
        elif 'wiccan' in message.content:
            await message.channel.send('Wiccan is inferior to I')
        elif 'Funsies' in message.content:
            await message.channel.send('Are you just trying to ruin Reubens life?')
        elif 'Dead chat' in message.content:
            await message.channel.send('Only dead because we are hiding from you.')

def setup(client):
    client.add_cog(Jayden(client))
