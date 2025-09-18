import discord
from discord.ext import commands
import json
import logging
import Commands.RandomCat as CatCommand
import Commands.Randome as Randome

handler = logging.FileHandler(filename='discordchan.log', encoding='utf-8', mode='w')

# Config
with open('config.json') as co:
    config = json.load(co)

# Bot Setup
bot = commands.Bot(command_prefix=config.prefix)

# unsure if needed
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Client(intents=intents)


@bot.event
async def on_ready(self):
    print(f'We have logged in as {bot.user}')

# region Commands

# Not needed?
# @bot.command()
# async def help(self, ctx):
#     await ctx.send(f'List of commands:'
#                    f'- {config.prefix}ping'
#                    f'- {config.prefix}cat'
#                    f'- {config.prefix}randime'
#                    f'- {config.prefix}help')


@bot.command()
async def ping(self, ctx):
    await ctx.send('pong')


@bot.command()
async def cat(self, ctx):
    await CatCommand.RandomCat().get_cat_url()


@bot.command()
async def randome(self, ctx):
    await Randome.Randome(config).get_random_image()

# endregion

bot.run(config["discord_token"], handler)


