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
from . import __version__

from discord import Colour
from discord import Activity
from discord import ActivityType
from discord import Status

# fmt: off
BOT_ACTIVITY = Activity(
    name=f"v{__version__}",
    type=ActivityType.listening
)
# fmt: on
BOT_STATUS = Status.idle

EMBED_STANDART_COLOUR = Colour.from_rgb(188, 172, 155)

EMBED_ERROR_TITLE = "Ошибка!"
EMBED_ERROR_COLOUR = Colour.from_rgb(255, 75, 75)

CONFIG_PATH = "./config.json"

TIPS = [
    "У вас есть 3 минуты на выбор радио-станции",
    "Вы можете выбрать страну и язык радио-станции",
    "Перед тем как уйдете не забудьте выключить радио /stop"
]
