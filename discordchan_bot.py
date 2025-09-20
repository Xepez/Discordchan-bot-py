import discord
from discord.ext import commands
import logging

import Voice.Voice as Voice

import json
import asyncio
import youtube_dl

import Commands.RandomCat as CatCommand
import Commands.RandomPicture as RandomeCommand


handler = logging.FileHandler(filename='discordchan.log', encoding='utf-8', mode='w')

# region Bot Setup


# Config
with open('config.json') as co:
    config = json.load(co)

intents = discord.Intents.default()
intents.message_content = True  # needed?

# Help
help_command = commands.DefaultHelpCommand(no_category='Commands')

bot = commands.Bot(intents=intents, command_prefix=config['prefix'], help_command=help_command)

# Voice
voice = Voice.Voice(config)

# endregion

# region Events


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# endregion

# region Commands


@bot.command(brief="Pong")
async def ping(ctx):
    await ctx.send('pong')


@bot.command(brief="Nick")
async def nick(ctx):
    await ctx.send(content='Nick is a is a great human and I cherish his friendship', tts=True)


@bot.command(brief="Cat Picture")
async def cat(ctx):
    cat_obj = CatCommand.RandomCat()
    if cat_obj is None:
        await ctx.send(config["default_error"] + 'cat image')

    await ctx.send(cat_obj.url)


@bot.command(brief="Anime Picture")
async def randome(ctx):
    randome_obj = RandomeCommand.Randome(config)
    if randome_obj is None:
        await ctx.send(config["default_error"] + 'random anime image')

    await ctx.send(await randome_obj.get_random_image())


@bot.command(brief="Anime Picture V2")
async def randome2(ctx):
    randome_obj = RandomeCommand.Randome(config)
    if randome_obj is None:
        await ctx.send(config["default_error"] + 'random image')

    await ctx.send(await randome_obj.get_random_image_2())


#  TODO
@bot.command(brief="Play a song")
async def play(ctx, url):
    if url.startswith("https://www.youtube.com/watch?v="):
        channel = ctx.message.author.voice.channel
        await voice.play_yt_link(channel, url)
    else:
        ctx.send("Not a valid url")


@bot.command(brief="Disconnect Bot")
async def stop(ctx):
    await ctx.bot.voice_clients[0].disconnect()


@bot.command(brief="Play grunt yay")
async def play_url_test(ctx):
    # Get requesting users channel and connect to it
    channel = ctx.message.author.voice.channel
    await voice.play_file(channel, config["test_sound_path"])


# endregion

bot.run(config["discord_token"], log_handler=handler)


