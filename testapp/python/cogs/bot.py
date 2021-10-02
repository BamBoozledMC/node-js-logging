import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
client = commands.Bot(command_prefix = 'r!')
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)
noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'
guild_ids = [702333016948736022, 874318705817968710]
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_option, create_choice

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('COG is loaded.')



def setup(client):
    client.add_cog(Bot(client))