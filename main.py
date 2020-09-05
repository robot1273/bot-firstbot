$ heroku buildpacks:set heroku/php

#discord bot - first bot
import discord
from discord.ext import commands
import random
from random import randint
import time
import sys
token = "NzUxNDc5NzE5ODMyMDU5OTk1.X1JsBw.oqiSEkoBMXFP793txI200_qZN0w"

client = commands.Bot(command_prefix = ">>")

#
insults = [" is quite dumb"," is now roasted"," is a poopyhead"," is an idiot"," is not kind"," is an uneducated swine"," has lost all their braincells"," never had a brain"," is too cool to be roasted"]
#

@client.event
async def on_ready():
    print("Bot is ready")
    
@client.event
async def on_member_join(member):
    print(member,"has joined a server.")

@client.event
async def on_member_remove(member):
    print(member,"has left a server.")

@client.command()
async def roast(ctx, person):
    if person == "robot":
        await ctx.send("you fool, robot is too epic")
    else:
        await ctx.send(person+random.choice(insults))

@client.command()
async def rate(ctx, person):
    rating = randint(0,10)
    if person == "robot":
        rating = "69 ha ha .-."
    rating = str(rating)
    await ctx.send("id rate "+person+" a "+rating)
    rating = int(rating)
    if rating == 0:
        await ctx.send("nub")
    elif rating < 2:
        await ctx.send("you suck")
    elif rating <= 5 and rating > 2:
        await ctx.send("you are eh")
    elif rating <= 8 and rating > 5:
        await ctx.send("you are pretty cool i guess")
    elif rating <= 10 and rating > 8:
        await ctx.send("epico")

    
    
client.run(token)
