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

from discord import ApplicationContext, VoiceClient, Embed

from discord.ext.bridge import bridge_command
from discord.ext.bridge import Bot
from discord.ext.commands import Cog


class Stop(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @bridge_command(description="Выключить радио")
    async def stop(self, ctx: ApplicationContext) -> None:
        client: VoiceClient = ctx.voice_client

        if client.is_connected():
            # Stop music and disconnect from the voice channel
            client.stop()
            await client.disconnect()

        # Embed
        title = "📻 ┊ Радио"
        description = "❌ Радио выключено!"

        # fmt: off
        embed = Embed(
            title=title,
            description=description,
            colour=EMBED_STANDART_COLOUR
        )
        # fmt: on
        embed.set_footer(text=f"СОВЕТ: {choice(TIPS)}")

        await ctx.respond(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(Stop(bot))
