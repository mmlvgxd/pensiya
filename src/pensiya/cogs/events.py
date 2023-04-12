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
from traceback import print_exception
from ..constants import EMBED_ERROR_COLOUR, EMBED_ERROR_TITLE
from ..logger import logger

from discord import ApplicationContext, DiscordException, Embed, Interaction

from discord.ext.bridge import Bot
from discord.ext.commands import Cog


class Events(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    # Called when the client has successfully connected to Discord
    async def on_connect(self) -> None:
        await self.bot.sync_commands()

        logger.info(f"Bot {self.bot.user.name} connected")

    @Cog.listener()
    # Called when the client has disconnected from Discord,
    # or a connection attempt to Discord has failed
    async def on_disconnect(self) -> None:
        logger.warn(f"Bot {self.bot.user.name} disconnected")

    @Cog.listener()
    # Called when the client is done preparing the data received from Discord
    async def on_ready(self) -> None:
        logger.info(f"Bot {self.bot.user.name} is ready")

    @Cog.listener()
    # Called when the client has resumed a session.
    async def on_resumed(self) -> None:
        logger.info(f"Bot {self.bot.user.name} has resumed a session")

    @Cog.listener()
    # Called when a particular shard ID has resumed a session
    async def on_shard_connect(self, shard_id) -> None:
        logger.info(f"Shard {shard_id} connected")

    @Cog.listener()
    # Called when when a particular shard ID has disconnected from Discord.
    async def on_shard_disconnect(self, shard_id) -> None:
        logger.warn(f"Shard {shard_id} disconnected")

    @Cog.listener()
    # Called when a particular shard ID has become ready
    async def on_shard_ready(self, shard_id) -> None:
        logger.info(f"Shard {shard_id} is ready")

    @Cog.listener()
    # Called when a particular shard ID has resumed a session
    async def on_shard_resumed(self, shard_id) -> None:
        logger.info(f"Shard {shard_id} has resumed a session")

    @Cog.listener()
    # Called when an application command has an error.
    async def on_application_command_error(
        self,
        # fmt: off
        context: ApplicationContext,
        exception: DiscordException
        # fmt: on
    ) -> None:
        class__ = exception.__class__
        name = class__.__name__
        traceback = exception.__traceback__

        print_exception(class__, exception, traceback)

        # Embed
        description = f"`{name}`: `{exception}`"

        # fmt: off
        embed = Embed(
            colour=EMBED_ERROR_COLOUR,
            title=EMBED_ERROR_TITLE,
            description=description
        )
        # fmt: on

        await context.respond(embed=embed)

    # fmt: off
    @Cog.listener()
    async def on_unknown_application_command(
        interaction: Interaction
    ) -> None:
        logger.info(f"Unknown interaction: {interaction}")
    # fmt: on


def setup(bot: Bot) -> None:
    bot.add_cog(Events(bot))
