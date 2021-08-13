import discord
import os
from discord import guild
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from dotenv import load_dotenv
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'
guild_ids = [702333016948736022, 874318705817968710, 860667007632277524]
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
        await ctx.send('**Curret Command List:** \n`/help` - Shows this menu. \n`/info` - Gives info on how to join the smp. \n`/apply` - Shows how to apply for the server. \n`/ping` - Shows the ping in ms to the server. \n`/purge <amount>` - Deleted the specified number of messages. \n`/eval <amount> <symbol> <amount>` - Solves your greatest math problems. \n`/bubblewrap` - Pop some bubbles!')


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
        embed=discord.Embed(title="**How to join the Ramen SMP!**", description="This is a Nation's SMP where you and your friends can gather resources, start wars and become the most powerful nation Minecraft has seen.  \n \nTo apply for the server, go run /apply!  \n \nThe server IP is: **51.81.48.184:25585**  \n \nIf you have any questions, DM one of the staff!   Yours sincerely, The Ramen SMP Staff Team.", color=0xe60d43)
        await ctx.send(embed=embed)

        
    @cog_ext.cog_slash(name="Apply", description="Get info on how to be whitelisted on the Ramen SMP.", guild_ids=guild_ids)
    async def apply(self, ctx: SlashContext):
        await ctx.send("**First, to join the server, you must apply. Here is the link! https://forms.gle/3BES6WgUQmkM37do7** \nOnce you are done, it should take about 10 minutes to get whitelisted. If you are having issues, DM Loudbook!")



def setup(client):
    client.add_cog(Slash(client))
