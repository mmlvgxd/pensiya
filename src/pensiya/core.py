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
from .modules.config import Config
from .logger import logger
from .modules.radio import search

from discord import (
    Bot,
    # UI
    Interaction,
    SelectOption,
    # Voice
    VoiceChannel,
    VoiceClient,
    FFmpegPCMAudio,
    # Embed
    Embed,
    Colour
)
from discord.ui import Select, View


bot = Bot(Config.PREFIX)


@bot.event
async def on_connect() -> None:
    logger.info("The bot is connected to Discord")


@bot.event
async def on_ready() -> None:
    logger.info("The bot is ready to use")


@bot.command()
async def ping(ctx) -> None:
    await ctx.respond("pong")


@bot.command()
async def play(ctx, name: str) -> None:
    # Components callback
    async def selectCallback(interaction: Interaction) -> None:
        # Radio
        index: str = select.values[0]
        station: dict = stations[int(index)]
        name: str = station["name"]
        url: str = station["url"]

        # I'm lazy
        name = (
            name
            .replace('\n', '')
            .replace('\t', '')
        )

        # Voice
        channel: VoiceChannel = ctx.author.voice.channel
        client: VoiceClient = await channel.connect()

        # If the radio is already playing then restart
        if client.is_playing():
            client.stop()

        client.play(FFmpegPCMAudio(url), after=lambda error: print(error))

        # Embed
        description = f"✅ Радио включено!\n\n🎶 Сейчас играет `{name}`..."

        # fmt: off
        embed = Embed(
            colour=colour,
            title=title,
            description=description
        )
        # fmt: on

        await interaction.response.send_message(embed=embed)

    stations: list[dict] = search(name)

    # fmt: off
    select = Select(
        placeholder="Выберите станцию...",
        options=[
            SelectOption(
                label=station["name"],
                value=str(stations.index(station)),
                description=station["stationuuid"]
            )
            for station in stations
        ]
    )
    # fmt: on

    # Components
    select.callback = selectCallback
    view = View(select)

    # Embed
    title = "📻 ┊ Радио"
    description = f"🔎 Нашлось `{len(stations)}`/`10` станций по запросу `{name}`"

    colour = Colour.from_rgb(188, 172, 155)

    # fmt: off
    embed = Embed(
        title=title,
        description=description,
        colour=colour
    )
    # fmt: on

    await ctx.respond(embed=embed, view=view)


@bot.command()
async def stop(ctx) -> None:
    # Voice
    client: VoiceClient = ctx.voice_client

    await client.stop()
    await client.disconnect()
    # Embed
    title = "📻 ┊ Радио"
    description = "❌ Радио выключено"

    colour = Colour.from_rgb(188, 172, 155)

    # fmt: off
    embed = Embed(
        title=title,
        description=description,
        colour=colour
    )
    # fmt: on

    await ctx.respond(embed=embed)