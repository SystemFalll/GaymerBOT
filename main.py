'''

This code was written by SystemFall

GaymerBOT
Mainly a reaction based role bot

To Do:
	Almost everything
    --- Ping command

'''

import discord
import os
from replit import db
from discord.ext import commands
from discord.ext.commands import has_permissions

token = os.environ['token']
client = commands.Bot(command_prefix = "'")

@client.event
async def on_ready():
    print(f'BOT enabled as {client.user}!')

@client.command()
async def ping(ctx):
	if ctx.author == client.user:
		return

	await ctx.send(f'Pong! {round(client.latency)}')

client.run(token)
	
