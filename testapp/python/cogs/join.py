
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot(command_prefix = 'rb!')
class Join(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Join cog is loaded.')
""""
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 854156802325479434:
            return
        elif message.author.id == 845383239043514388:
            return        
        else:
            print('Sending join message')
            await message.channel.send('**To join the Ramen SMP, type /info!** \n*Sent because of keyword "join"*')
            await client.process_commands(message)            
"""
def setup(client):
    client.add_cog(Join(client))
