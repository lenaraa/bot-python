# CuteBot by Lenaraa

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
from tokens import token
import os

#client = discord.Client()
bot_prefix=("!", "?")
bot = Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print("Bot online !")
    print("Name : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))

@bot.command(name='cute',
             description="Envoie une photo d'un animal mignon.",
             brief="Fais le plein de mignonitude !")
async def cute():
    #await bot.say("image")
    dir_fd = os.open('pic', os.O_RDONLY)
    def opener(path, flags):
        return os.open(path, flags, dir_fd=dir_fd)
    liste=os.listdir("/pic")
    image=random.choice(liste)
    with open(image, 'rb', opener=opener) as f:
        await bot.send_file(discord.Channel, f)
    os.close(dir_fd) 
    #await bot.say(random.randrange(100))


@bot.command(name='ping',
             description="Envoie ping",
             brief="Ping pong")
async def ping():
    await bot.say("Pong !")


@bot.command(name='8ball',
             description="Répond à une question en oui ou non.",
             brief="Laisse l'univers décider.",
             aliases=['eight_ball', 'eightball', '8-ball'])
async def eight_ball():
    possible_resp = [
        'Essaye plus tard',
        'Essaye encore ',
        'Pas d\'avis ',
        'C\'est ton destin',
        'Le sort en est jeté',
        'Une chance sur deux ',
        'Repose ta question ',
        'D\'après moi oui ',
        'C\'est certain',
        'Oui absolument',
        'Tu peux compter dessus',
        ' Sans aucun doute ',
        'Très probable',
        'Oui',
        'C\'est bien parti',
        'C\'est non',
        'Peu probable',
        'Faut pas rêver',
        'N\'y compte pas',
        'Impossible'
    ]
    await bot.say(random.choice(possible_resp))


bot.run(token);
