import discord
import os
import time
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get
from discord_slash import SlashCommand, SlashContext
intents = discord.Intents().all()
client = commands.Bot(command_prefix = 'r!', intents=intents)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True, delete_from_unused_guilds=True)
noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'
guild_ids = [702333016948736022, 874318705817968710]
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_option, create_choice

bot = commands.Bot(command_prefix="r!", intents=intents)

WELCOME = os.getenv('WELCOME')


@client.event
async def on_message(message):
    if 'I agree to the terms and conditions.' in message.content:
        if message.channel.id == 880499886657765396:
            if message.author.id == 854156802325479434:
                await bot.process_commands(message)
                return
            else:
                await message.channel.send(f'Awesome! Giving you the role now!')
                await asyncio.sleep(2)
                member = get(message.guild.roles, name="Member")
                await message.author.add_roles(member)
                await asyncio.sleep(1)
                await message.delete()
        else:
            return
    elif message.channel.id == 880499886657765396:
        if message.author.id == 854156802325479434:
            await asyncio.sleep(10)
            await message.delete()
        else:
            await asyncio.sleep(5)
            await message.delete()
    else:
        return
    await client.process_commands(message)
# await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="The Ramen Bot! /help for assistance!"))

    

"""
@client.command()
async def hello(ctx):
    await ctx.send('Why hello there good human!')
"""

@client.command()
async def sendwelcome(ctx):
    await ctx.send("Hello there human! Welcome to the Ramen Survival Multiplayer (also known as the RSMP) Minecraft's best noodle inspired server. \n \nI’m Ramen bot (you can call me RBot) and it's my job to help you settle in here as quickly as possible. The first thing you’ll need to do is agree to our Discord Terms and Conditions posted Below. \n \n> #1: I agree to never bully, swear or insult any player or moderator at any time. \n> \n> #2: I agree to read the rules in the #rules channel when I join.\n> \n> #3: I agree to respect all members and staff. \n \n**If you agree type `I agree to the terms and conditions.` (__In exact words...__) in the chat!** \n \nTo get even more info on how to join, use /info! You will have to apply for the server before joining. To get the form, run /apply! \n \nHave a nice day!\nRSMP Staff Team")



@client.command()
async def kick(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send("Test")
    else:
        await ctx.send(noperms)



@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command()
async def load(ctx, extention):
    if ctx.message.author.guild_permissions.manage_messages:
        client.load_extension(f'cogs.{extention}')
        await ctx.send('Module loaded')

@client.command()
async def unload(ctx, extention):
    if ctx.message.author.guild_permissions.manage_messages:
        client.unload_extension(f'cogs.{extention}')
        await ctx.send('Module unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def purge(ctx, amount=50):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send(noperms)




@slash.slash(name="loadcog",
                description="Admins Only",
                guild_ids=guild_ids,
                default_permission=False, permissions={702333016948736022: [create_permission(664597683511492608, 2,True)]},
                options=[
                    create_option(
                        name="module",
                        description="Which module would you like to load?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="jayden",
                                value="jayden"
                            ),
                            create_choice(
                                name="slash",
                                value="slash"
                            ),
                            create_choice(
                                name="bot",
                                value="bot"
                            ),
                        ]
                    )
                ])
async def loadcog(ctx, module: str):
    await ctx.send('Module loaded')
    client.load_extension(f'cogs.{module}')

@slash.slash(name="unloadcog",
                description="Admins Only",
                guild_ids=guild_ids,
                default_permission=False, permissions={702333016948736022: [create_permission(664597683511492608, 2,True)]},
                options=[
                    create_option(
                        name="module",
                        description="Which module would you like to unload?",

                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="jayden",
                                value="jayden"
                            ),
                            create_choice(
                                name="slash",
                                value="slash"
                            ),
                            create_choice(
                                name="bot",
                                value="bot"
                            ),
                        ]
                    )
                ])
async def unload(ctx, module: str):
    client.unload_extension(f'cogs.{module}')
    await ctx.send('Module unloaded')



load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)