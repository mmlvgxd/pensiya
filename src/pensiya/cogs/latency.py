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
from ..constants import TIPS
from ..constants import EMBED_STANDART_COLOUR

from discord import ApplicationContext, Embed

from discord.ext.bridge import bridge_command
from discord.ext.bridge import Bot
from discord.ext.commands import Cog


class Latency(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @bridge_command(description="Посмотреть задержку бота")
    async def latency(self, ctx: ApplicationContext) -> None:
        _latency = round(self.bot.latency * 1000)

        # Embed
        title = "Задержка"
        description = f"{_latency} миллисекунд"

        # fmt: on
        embed = Embed(
            colour=EMBED_STANDART_COLOUR,
            title=title,
            description=description
        )
        # fmt: off
        embed.set_footer(text=f"СОВЕТ: {choice(TIPS)}")

        await ctx.respond(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(Latency(bot))
