import random
import requests
import discord
import valve 

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!") # can use tuple for multiple command prefixes
TOKEN = 'DISCORD TOKEN GOES HERE'
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
async def on_ready():
    await client.change_presence(game=Game(name= "Join Sim 2018"))
    print("Logged in as " + client.user.name)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)


#figure out if pulling from battlemetrics is more accurate than querying the server directly
#------------------------------------Use Cases----------------------------------------
# display numbers of players on server every 60 min
# if prompted display a list of names of players on server and how long they've been online(Name, Duration)
# if 5 or more players join within 6 minutes post an alert
# if server pop is greater than 25 post an update every 5 min until server pop drops below 25
# if server is being DDOSed display an alert
# if the command grief is entered post that the server is under attack, server pop until the command oly oly oxen free is entered.
# take steam-IDs as input somehow and create a blacklist of known baddies.











client.run(TOKEN)

