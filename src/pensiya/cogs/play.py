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
from random import choice
from ..modules.radio import search
from ..constants import TIPS
from ..constants import EMBED_STANDART_COLOUR

from discord import (
    ApplicationContext,
    VoiceChannel,
    VoiceClient,
    FFmpegPCMAudio,
    Embed,
    SelectOption,
    Interaction,
    Option,
)

from discord.ext.bridge import bridge_command
from discord.ext.bridge import Bot
from discord.ext.commands import Cog

from discord.ui import Select, View


class Play(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @bridge_command(description="Включить радио")
    async def play(
        self,
        ctx: ApplicationContext,
        name: Option(str, "Название радио-станции"),
        country: Option(str, "Страна радио-станции", required=False, default=""),
        language: Option(str, "Язык радио-станции", required=False, default=""),
    ) -> None:
        # Components callback
        async def selectCallback(interaction: Interaction) -> None:
            # Radio
            index: str = select.values[0]
            station: dict = stations[int(index)]
            name: str = station["name"]
            url: str = station["url"]

            # I'm lazy
            # fmt: off
            name = (
                name
                .replace("\n", "")
                .replace("\t", "")
            )
            # fmt: on

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
                colour=EMBED_STANDART_COLOUR,
                title=title,
                description=description
            )
            # fmt: on
            embed.set_footer(text=f"СОВЕТ: {choice(TIPS)}")

            await interaction.response.send_message(embed=embed)

        stations: list[dict] = search(name, country, language)

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

        # fmt: off
        embed = Embed(
            title=title,
            description=description,
            colour=EMBED_STANDART_COLOUR
        )
        # fmt: on
        embed.set_footer(text=f"СОВЕТ: {choice(TIPS)}")

        await ctx.respond(embed=embed, view=view)


def setup(bot: Bot) -> None:
    bot.add_cog(Play(bot))
