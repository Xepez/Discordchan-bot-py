import discord
from discord.ext import commands
import json
import requests

# TODO:
# Add anime piracy link
# Add hentai cmd
# Add cat cmd

with open('config.json') as co:
	config = json.load(co)


bot = commands.Bot(command_prefix = '!')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

bot.run(config["discord_token"])
