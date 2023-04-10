# MIT License
#
# Copyright (c) 2023 mmlvgx
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from re import search
from asyncio import TimeoutError
from .modules.radio import search as _search
from .modules.config import Config
from .logger import logger

from discord import FFmpegPCMAudio
from discord.ext import commands
from discord_ui import UI, SlashOption
from discord_ui import SelectMenu, SelectOption


bot = commands.Bot(Config.PREFIX)
ui = UI(bot)


# Events
@bot.event
async def on_connect() -> None:
    logger.info("The bot is connected to the discord")


@bot.event
async def on_ready() -> None:
    logger.info("The bot is ready to use")


# Commands
@ui.slash.command("ping", "Пинг")
async def ping(ctx) -> None:
    await ctx.respond("pong")


@ui.slash.command(
    "play",
    "Включить станцию",
    options=[SlashOption(str, "name", "Название", required=True)],
)
async def play(ctx, name: str) -> None:
    placeholder = "Выберите станцию"

    channel = ctx.author.voice.channel

    stations = _search(name)
    _stations = {}
    options = []

    for station in stations:
        uuid = station["stationuuid"]
        name = station["name"]
        url = station["url"]

        _stations[uuid] = url
        options.append(SelectOption(uuid, f"{name} ({uuid})"))

    # fmt: off
    message = await ctx.send(components=[SelectMenu(
        options=options, placeholder=placeholder
    )])
    # fmt: on

    try:
        select = await message.wait_for("select", bot, by=ctx.author, timeout=60)
        content = str([x.content for x in select.selected_options])
        stationuuid = search(r'\((.*?)\)', content)

        url = _stations[stationuuid.groups()[0]]

        await message.reply('Играет')

        voice = await channel.connect()
        voice.play(FFmpegPCMAudio(url)) # Не включается


    except TimeoutError:
        await message.delete()
