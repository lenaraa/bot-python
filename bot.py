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


#Message dans le terminal quand on lance le bot
@bot.event
async def on_ready():
    print("Bot online !")
    print("Name : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))


@bot.command(pass_context=True,
             name='cute',
             description="Envoie une photo au hasard parmis le dossier ./pic",
             brief="Envoie une photo d'animal",
             aliases=['mignon', 'animal'])
async def cute(ctx):
    l = os.listdir("./pic")
    img = random.choice(l)
    with open("./pic/" + img, 'rb') as f:
        await bot.send_file(ctx.message.channel, f)
        
        
@bot.command(pass_context=True,
             name='joke',
             description="Envoie une ligne au hasard parmis le fichier joke.txt",
             brief="Envoie une blague carambar",
             aliases=['blague', 'carambar'])
async def joke(ctx):
    liste = []
    with open('joke.txt', 'r') as f :
        for l in f.readlines() :
            liste.append(l)
        f.close()
    l = random.choice(liste)
    await bot.say(l)


@bot.command(name='ping',
             description="Envoie ping",
             brief="Ping pong")
async def ping():
    await bot.say("Pong !")


@bot.command(name='8ball',
             description="Répond à une question en oui ou non au hasard.",
             brief="Laisse l'univers décider.",
             aliases=['eight_ball', 'eightball', '8-ball', 'reponse', 'réponse'])
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
