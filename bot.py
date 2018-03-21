# CuteBot by Lenaraa

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
from tokens import token

client = discord.Client()
bot_prefix="!"
bot = Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print("Bot online !")
    print("Name : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong !")

@bot.command(pass_context=True)
async def cute(ctx):
    pass
    await bot.say("image")
    #await bot.say(random.randrange(100))


bot.run("token");
