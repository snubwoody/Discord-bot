from http import client
import discord
import json
import requests
from bs4 import BeautifulSoup

with open('config.json') as data:
 cnfg = json.load(data)
 token = cnfg['token']
    
client = discord.Client()

#function to get the raw html of a website
def get(url):
    
    #requests the url
    page = requests.get(url)
    #returns the page content as html
    global scraper
    scraper = BeautifulSoup(page.content, 'html.parser')
    
    
    
get("https://za.ign.com/article/news?keyword__type=game")


links = []
def parse():
    #gets all the divs with m as thier class name
    val = scraper.find_all("div","m")
    
    #gets the specified elements and puts them in arrays
    for a in val:
        links.append(a.h3.a['href'])
    
    
parse()





#runs when the bot is connected and ready
@client.event
async def on_ready():
   print('Logged on as {0}!'.format(client))
   chn = client.get_channel(967332199403782164)
   await chn.send('please work')
   await chn.send(f"{links[1]}")


#runs everytime a message is detected
@client.event
async def on_message(message):
   channel = message.channel
   print('Message from {0.author}: {0.content}'.format(message))
      
   if message.content.startswith('$marco'):
      await channel.send('polo')
   elif message.content == "fuck":
      await channel.send('no cursing')
   elif message.content == "charlemagne":
      await channel.send("Please dont disurb me, I'm busy")
 
client.run(token) 


