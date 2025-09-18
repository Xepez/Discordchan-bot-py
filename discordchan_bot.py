import discord
from discord.ext import commands
import json
import logging
import Commands.RandomCat as CatCommand
import Commands.RandomPicture as Randome

handler = logging.FileHandler(filename='discordchan.log', encoding='utf-8', mode='w')

# region Bot Setup


# Config
with open('config.json') as co:
    config = json.load(co)


intents = discord.Intents.default()
intents.message_content = True

help_command = commands.DefaultHelpCommand(no_category='Commands')

bot = commands.Bot(intents=intents, command_prefix=config['prefix'], help_command=help_command)


# endregion

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


@bot.command(brief="Pong")
async def ping(ctx):
    await ctx.send('pong')


@bot.command(brief="Returns a picture of a cat")
async def cat(ctx):
    cat_obj = CatCommand.RandomCat()
    if cat_obj is None:
        await ctx.send(config["default_error"] + 'cat image')

    await ctx.send(cat_obj.url)


@bot.command(brief="Returns a picture")
async def randome(ctx):
    randome_obj = Randome.Randome(config)
    if randome_obj is None:
        await ctx.send(config["default_error"] + 'random anime image')

    await ctx.send(await randome_obj.get_random_image())


@bot.command(brief="NEW - Returns a picture")
async def randome2(ctx):
    randome_obj = Randome.Randome(config)
    if randome_obj is None:
        await ctx.send(config["default_error"] + 'random image')

    await ctx.send(await randome_obj.get_random_image_2())

# endregion

bot.run(config["discord_token"], log_handler=handler)


