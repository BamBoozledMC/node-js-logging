import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
client = commands.Bot(command_prefix = 'r!')
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)
noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'
guild_ids = [702333016948736022, 874318705817968710, 860667007632277524]
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_option, create_choice


bot = commands.Bot(command_prefix="r!")


@client.event
async def on_message(message):
    if 'join' in message.content:
        if message.author == client.user:
            return
        elif message.author.id == 845383239043514388:
            return
        else:
            print('Sending join message')
            await message.channel.send('**To join the Ramen SMP, type /info!** \n*Sent because of keyword "join"*')
            await client.process_commands(message)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="The Ramen Bot! /help for assistance!"))
    print ('Bot is ready!')

@client.command()
async def hello(ctx):
    await ctx.send('Why hello there good human!')


@client.command()
async def kick(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send("Test")
    else:
        await ctx.send(noperms)

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

for filename in os.listdir('./python/cogs'):
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
