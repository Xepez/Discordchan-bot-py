import json
import discord
import youtube_dl  # TODO: NEED TO CHANGE TO yt-dlp due to deprecation


# Config
with open('config.json') as co:
    config = json.load(co)

youtube_dl.utils.bug_reports_message = lambda: ''

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(id).mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
# --Other potential options
# 'format': 'bestaudio/best',
# 'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
# 'restrictfilenames': True,
# 'noplaylist': True,
# 'nocheckcertificate': True,
# 'ignoreerrors': False,
# 'logtostderr': False,
# 'quiet': True,
# 'no_warnings': True,
# 'default_search': 'auto',
# 'source_address': config["ipv4"],  # bind to ipv4 since ipv6 addresses cause issues sometimes


class Voice:

    def __init__(self, channel=None):
        self.current_channel = channel

    async def play_yt_link(self, channel, url):
        vc = await self._channel_connect(channel)
        if vc is None:
            return config["default_error"] + 'channel'

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
            except Exception as e:
                e=e

        file_path = ydl

        # play audio
        vc.play(discord.FFmpegPCMAudio(source=file_path, executable=config["ffmpeg_windows_path"]))

        # clean up


    async def play_file(self, channel, file_path):
        vc = await self._channel_connect(channel)
        if vc is None:
            return config["default_error"] + 'channel'

        vc.play(discord.FFmpegPCMAudio(source=file_path, executable=config["ffmpeg_windows_path"]))
        return None

    # Private Functions
    async def _channel_connect(self, new_channel):
        await self._sync_channel(new_channel)

        if self.current_channel is not None:
            return await discord.VoiceChannel.connect(self.current_channel)
        else:
            return None

    async def _sync_channel(self, new_channel):
        if new_channel is not None and self.current_channel != new_channel:
            self.current_channel = new_channel
