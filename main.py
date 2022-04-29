from http import client
import discord
import json

data = open('config.json')

cnfg = json.load(data)

token = cnfg['token']

data.close()


class Myclient(discord.Client):
 async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))


 async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message.content.startswith('$marco'):
        channel = message.channel
        await channel.send('polo')
                  

client = Myclient()
client.run(token)
