import discord
from discord.ext import commands
import json
import requests

with open('config.json') as co:
	config = json.load(co)


bot = commands.Bot(command_prefix = '!')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

bot.run(config["discord_token"])