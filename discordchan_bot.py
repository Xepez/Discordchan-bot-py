import discord
from discord.ext import commands
import json
import logging
import Commands.RandomCat as CatCommand
import Commands.RandomPicture as Randome

handler = logging.FileHandler(filename='discordchan.log', encoding='utf-8', mode='w')

# Config
with open('config.json') as co:
    config = json.load(co)

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix=config['prefix'])


@bot.event
async def on_ready():
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
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def cat(ctx):
    cat_obj = CatCommand.RandomCat()
    if cat_obj is None:
        await ctx.send(config["default_error"] + 'cat image')

    await ctx.send(cat_obj.url)


@bot.command()
async def randome(ctx):
    randome_obj = Randome.Randome(config)
    if randome_obj is None:
        await ctx.send(config["default_error"] + 'random anime image')

    await ctx.send(await randome_obj.get_random_image())

# endregion

bot.run(config["discord_token"], log_handler=handler)


