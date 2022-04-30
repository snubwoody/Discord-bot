from http import client
import discord
import json
from discord.ext import tasks
from discord.ext import commands



with open('config.json') as data:
 cnfg = json.load(data)
 token = cnfg['token']
    


client = discord.Client()



@client.event
async def on_ready():
   print('Logged on as {0}!'.format(client))

@client.event
async def on_message(message):
   print('Message from {0.author}: {0.content}'.format(message))
   if message.content.startswith('$marco'):
      channel = message.channel
      await channel.send('polo')


async def d():
   chn = client.get_channel(967332199403782164)
   await chn.send("pleaseeeee")
   

      

    
                  


client.run(token)