import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get

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
        elif 'bad bot' in message.content:
            await message.channel.send('you know humans are not as smart as robots... right? if you dont then you need to get help.')
        elif 'Bad bot' in message.content:
            await message.channel.send('you know humans are not as smart as robots... right? if you dont then you need to get help.')
        elif "<" in message.content:
            await message.channel.send(">")
        elif ">" in message.content:
            await message.channel.send("<")
"""        
        elif 'I agree to the terms and conditions.' in message.content:
            member = message.author
            var = discord.utils.get(message.guild.roles, name = "Member")
            member.add_role(var) 
            await message.channel.send(f'{member} Awesome! Giving you the role now!')
            time.sleep(2)
"""
"""
    @commands.Cog.listener()
    async def on_message(self, ctx):
        ctx = await bot.get_context(message)
        if 'I agree to the terms and conditions.' in message.content:
            ctx = await bot.get_context(message)
            member = ctx.message.author
            role = discord.utils.get(lambda role: role.name == "Member", ctx.guild.roles) 
            await member.add_roles(role) 
            await ctx.send(f'{member} Awesome! Giving you the role now!')
            time.sleep(2)

        elif 'I agree to the terms and conditions' in message.content:
            await message.channel.send('Awesome! Giving you the role now!')
"""
def setup(client):
    client.add_cog(Jayden(client))