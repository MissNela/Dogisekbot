import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = "S!")

client.remove_command('help')



@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: S!, s!"))
    print("The bot is online and connected with Discord!") 
    await client.send_message(channel, "``Jsem tu a připraven!!``")
    


@client.event
async def on_message(message):
    
    channel = message.channel
    r = random.choice
    
    
    if message.content.upper() == "DOGISEK BOT":
        embed = discord.Embed(title = "Dogisek bot!", color = 0x311B92)
        embed.add_field(name="Muj prefix je",value="``>``!",inline=False)
        await client.send_message(message.channel, embed=embed)

client.run(os.getenv("BOT"))
