import discord
import os
import time
import string
import random
import aiohttp
from discord import guild
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from dotenv import load_dotenv
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'
guild_ids = [702333016948736022, 874318705817968710]
from discord_slash.utils.manage_commands import create_option

from discord.ext.commands import Bot
client = Bot(command_prefix = "r!")





def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client


    @cog_ext.cog_slash(name="Ping", description="Get the latency of the bot!", guild_ids=guild_ids)
    async def ping(self, ctx: SlashContext):
      await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
    
    @cog_ext.cog_slash(name="Bubblewrap", description="Pop some bubbles!", guild_ids=guild_ids)
    async def bubblewrap(self, ctx: SlashContext):
        await ctx.send('||POP||||POP||||POP||||POP||||POP||||POP||||POP||\n||POP||||POP||||POP||||POP||||POP||||POP||||POP||\n||POP||||POP||||POP||||POP||||POP||||POP||||POP||\n||POP||||POP||||POP||||POP||||POP||||POP||||POP||')

    @cog_ext.cog_slash(name="Help", description="Stop. Get help. From the bot!", guild_ids=guild_ids)
    async def help(self, ctx: SlashContext):
        await ctx.send('**Curret Command List:** \n`/help` - Shows this menu. \n`/info` - Gives info on how to join the smp. \n`/apply` - Shows how to apply for the server. \n`/ping` - Shows the ping in ms to the server. \n`/purge <amount>` - Deleted the specified number of messages. \n`/eval <amount> <symbol> <amount>` - Solves your greatest math problems. \n`/bubblewrap` - Pop some bubbles!. \n`/rickroll` - No explanation necessary.')


    @cog_ext.cog_slash(name="Purge", 
                        description="Deleted the specified number of messages.",
                        guild_ids=guild_ids,
                        options=[
                            create_option(
                                name='amount',
                                description='Number of messages to delete.',
                                option_type=4,
                                required=True
                            )
                        ]
    )
    async def purge(self, ctx: SlashContext, amount: int):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount)
            await ctx.send('Purge successful!')
            time.sleep(5)
            await ctx.message.delete()
        else:
            await ctx.send(noperms)

    @cog_ext.cog_slash(name="Eval", 
                        description="Solves your greatest math problems.",
                        guild_ids=guild_ids,
                        options=[
                            create_option(
                                name='amount',
                                description='First number',
                                option_type=4,
                                required=True
                            ),
                            create_option(
                                name='symbol',
                                description='Oporation (Accepts +, -, *, and /)',
                                option_type=3,
                                required=True
                            ),
                            create_option(
                                name='second_amount',
                                description='Second number',
                                option_type=4,
                                required=True
                            )                            
                        ]
    )
    async def eval(self, ctx: SlashContext, amount = float, symbol = float, second_amount = float):
        if symbol == '+':
            add_func = f"{amount} + {second_amount} = {add(amount, second_amount)}"
            await ctx.send(add_func)

        elif symbol == '-':
            subtract_func = f"{amount} - {second_amount} = {subtract(amount, second_amount)}"
            await ctx.send(subtract_func)

        elif symbol == '*':
            multiply_func = f"{amount} * {second_amount} = {multiply(amount, second_amount)}"
            await ctx.send(multiply_func)

        elif symbol == '/':
            divide_func = f"{amount} / {second_amount} = {divide(amount, second_amount)}"
            await ctx.send(divide_func)


    
    @cog_ext.cog_slash(name="Send", description="Sends the specified message.", guild_ids=guild_ids)
    async def send(self, ctx: SlashContext, message):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.send(message)
        else:
            await ctx.send(noperms)


    def add(x, y):
        return x + y
    @cog_ext.cog_slash(name="Info", description="Summon a wonderful embed with all the info you need to join the Ramen SMP!", guild_ids=guild_ids)
    async def info(self, ctx: SlashContext):
        embed=discord.Embed(title="**How to join the Ramen SMP!**", description="This is a Nation's SMP where you and your friends can gather resources, start wars and become the most powerful nation Minecraft has seen.  \n \nTo apply for the server, go run /apply!  \n \nThe server IP is: **51.81.48.184:25585** \nThe server version is: **1.17.1** \n \nIf you have any questions, DM one of the staff!   Yours sincerely, The Ramen SMP Staff Team.", color=0xe60d43)
        await ctx.send(embed=embed)
        
    @cog_ext.cog_slash(name="RickRoll", description="You know...", guild_ids=guild_ids)
    async def rickroll(self, ctx: SlashContext):
        await ctx.send("https://i.imgur.com/a/PocJ5Yn")
        
    @cog_ext.cog_slash(name="Apply", description="Get info on how to be whitelisted on the Ramen SMP.", guild_ids=guild_ids)
    async def apply_test(self, ctx: SlashContext):
        await ctx.defer()
        await ctx.send("**First, to join the server, you must apply. Here is the link! https://forms.gle/3BES6WgUQmkM37do7** \nOnce you are done, it should take about 10 minutes to get whitelisted. If you are having issues, DM Loudbook!")
    """
    @cog_ext.cog_slash(name="Meme", description="Memez", guild_ids=guild_ids)
    async def meme(self, ctx: SlashContext):
        async with aiohttp.ClientSession() as cs:

            async with cs.get('https://meme-api.herokuapp.com/gimme/dankmemes') as r:

                res = await r.json()

                embed = discord.Embed(title="", color = ctx.author.color)

                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])

                await ctx.send(embed=embed, content=None)
    """
    @cog_ext.cog_slash(name="Meme", description="Memez", guild_ids=guild_ids)
    async def meme(ctx):
        embed = discord.Embed(title="", description="")
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
    @cog_ext.cog_slash(name="Hack", description="hack your friends... totally legit.", guild_ids=guild_ids, 
                            options=[
                            create_option(
                                name='user',
                                description='User to hack!',
                                option_type=6,
                                required=True
                            )
                        ]
    )
    async def hack(self, ctx: SlashContext, user: str):
        percentage = 0
        letters = string.ascii_letters
        user2 = str(user)
        message = await ctx.send(f"Initiating hack module... {percentage}%")
        while percentage < 100:

            percentage = percentage + 4
            
            await message.edit(content=f"Initiating hack module... {percentage}%")
        percentage = 0
        await message.edit(content=f"Starting hack!")
        time.sleep(5)

        percentage2 = 0
        while percentage2 < 100:

            percentage2 = percentage2 + 4

            await message.edit(content=f"Obtaining password... {percentage2}%")
        percentage2 = 0

        await message.edit(content=f"**ERROR 504: x07163b31**")
        time.sleep(7)
        await message.edit(content=f"Solving error.")
        time.sleep(8)
        await message.edit(content=f"Error resolved!")
        time.sleep(3)
        await message.edit(content=f"Hack successful.")
        time.sleep(2)
        letters = string.ascii_letters
        await ctx.send(f"{user2[:-5]}'s password is: " + "".join(random.choice(letters) for i in range(10)) )

        







def setup(client):
    client.add_cog(Slash(client))