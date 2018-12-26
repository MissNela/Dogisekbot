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

left = '⏪'
right = '⏩'

general1=discord.Embed(title="Příkazy pro všechny!",description="``>cat`` +Ukáže ti random obrázek kočki! :D ``>dog`` + Ukáže ti random obrázek psa! :D ``>server info`` + Ukáže ti info o serveru! ``>meme`` + Ukáže ti random meme! xD",color = 0x304FFE)
general2=discord.Embed(title="Připravuje se",description="------------------",color=0x304FFE)
mod1=discord.Embed(title="Příkazy pro moderátory+!",description="``>warn`` +Varuje hráče! ``>ban`` +Banuje uživatele! ``>kick`` +Vyhodí uživatele!", color = 0xFF3D00)
mod2=diecord.Embed(title="Připravuje se!",description="--------------------",color=0xFF3D00)

gen_cmd = (general1, general2)
  
mod_cmd = (mod1, mod2)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: > | Developer: JustNela#6666"))
    print("The bot is online and connected with Discord!") 
   # await client.send_message(channel, "``Jsem tu a připraven!!``")
    
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await client.send_message(user, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await client.send_message(user, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
    

@client.event
async def on_message(message):
    
    channel = message.channel
    r = random.choice
    user = message.author
    
    if message.content.upper() == "DOGISEK BOT":
        embed = discord.Embed(title = "Dogisek bot!", color = 0x311B92)
        embed.add_field(name="Muj prefix je",value="``>``!",inline=False)
        await client.send_message(channel, embed=embed)
    if message.content.upper() == ">HELP":
        
    
      author = message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Potřebuješ pomoc?')
      embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/FrRtyS6',inline = False)
      embed.add_field(name = 'React 🇲 ',value ='Ukáže ti příkazy pro Moderátory!.',inline = False)
      embed.add_field(name = 'React 🇬 ',value ='Ukáže ti příkazy pro všechny.',inline = False)
      dmmessage = await client.send_message(user, embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.send_message(channel, '📨 Podívej se do PM pro více informací {}'.format(message.author.mention)
      
      

client.run(os.getenv("BOT"))
