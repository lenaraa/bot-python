# CuteBot by Lenaraa

import discord
import random
import asyncio
from tokens import token
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix="!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot online !")
    print("Name : {}".format(client.user.name))
    print("ID : {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong !")

@client.command(pass_context=True)
async def cute(ctx):
    await client.say("image")
    #await client.say(random.randrange(100))


client.run("token");
