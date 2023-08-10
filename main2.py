
#importar todo lo necesario 

import discord

from discord.ext import commands

import random

#crear las incias

intents=discord.Intents.default()

intents.message_content=True

#crear una instancia de bot y definir el prefijo

bot =commands.Bot(command_prefix='$',intents=intents)

 
#lista de ideas para manualidades con plastico 

 
@bot.event

async def on_ready():

    print(f"inicio tu chat satifactoriamente ID: {bot.user.id}, Usuario, {bot.user}")

 
@bot.command()
async def reciclar(ctx):

   

    await ctx.send(f"bidón?")
@bot.command()
async def bidón_azul(ctx):


    await ctx.send(f"papel y cartón") @bot.command()
async def bidón_verde(ctx):


    await ctx.send(f"vidrio") 
bot.run("MTEyOTEwNzk0NTYwNzY2Nzc1Mg.GWtjHM.v58K2h_dEdlXNUh3dsuZFeJV59mhZi92F0lQuI")