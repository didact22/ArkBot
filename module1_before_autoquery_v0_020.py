import random
import asyncio
import requests
import discord 
import valve 
import valve.source
import valve.source.a2s
import valve.source.master_server

from discord import Game
from discord.ext.commands import Bot

RUNQUERY = True 





BOT_PREFIX = ("?", "!") # can use tuple for multiple command prefixes
TOKEN = 'BOT TOKEN GOES HERE'
#all caps are constants because this isn't C

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball', #name modifies the trigger for the function
                description= "Answers a yes or no question", #output for the verbose help command
                brief="Answers from the beyond", #output for regular help command
                aliases=['eight_ball','eights'], #alternate commands that will call the function
                pass_context=True) #if it needs to know the context from the command

async def eight_ball(context):#if using context, must be first argument into function
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    #await client.say(random.choice(possible_responses)) #no context or mention 
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_ready(): #background tasks go in here!
    await client.change_presence(game=Game(name= "Join Sim 2018"))
    print("Logged in as " + client.user.name)
    await queryTask()

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)

@client.command()
async def query88():
    address = ('85.190.152.82' , 27015) # TheCenter 88's host address and port 27015 is right do not use port 7777
    try: #(85.190.152.82,7777)
       with valve.source.a2s.ServerQuerier(address) as server:
         info = server.info()
         players = server.players()
    except valve.source.NoResponseError:
         await client.say("Server {}:{} timed out!".format(*address))
         #continue
    displayListName = []
    for player in players["players"]:
        if player["name"]:
            displayListName.append(player)
            duraSec = int(player["duration"])
            duraMin = duraSec/60
            duraHour = duraMin
            await client.say("{name} has been online for ".format(**player)  + str(duraHour) + " hours.")
    player_count = len(displayListName)
    await client.say(str(player_count) + "/70 players are online" ) 
    await client.say("{server_name}".format(**info))

#figure out if pulling from battlemetrics is more accurate than querying the server directly
#------------------------------------Use Cases----------------------------------------
# display numbers of players on server every 60 min
# if prompted display a list of names of players on server and how long they've been online(Name, Duration)
# if 5 or more players join within 6 minutes post an alert
# if server pop is greater than 25 post an update every 5 min until server pop drops below 25
# if server is being DDOSed display an alert
# if the command grief is entered post that the server is under attack, display server pop until the command !allclear is entered.
# take steam-IDs as input somehow and create a blacklist of known baddies.

async def queryTask():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Query sent!")
        await query88()
        await asyncio.sleep(10)









client.run(TOKEN)

