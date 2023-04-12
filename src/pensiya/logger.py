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
from juneberry import Logger
from juneberry import Theme, Color, Effect
from juneberry import Message, Timestamp, Module

# fmt: off
theme = Theme(
    Color.Converters.from_rgb(180, 190, 254),
    Color.Converters.from_rgb(137, 180, 250),
    Color.Converters.from_rgb(203, 166, 247),
    Color.Converters.from_rgb(250, 179, 135),
    Color.Converters.from_rgb(243, 139, 168),

    Module(
        Color.Converters.from_rgb(205, 214, 244),
        Effect.Standart.BOLD
    ),
    Message(
        Color.Converters.from_rgb(205, 214, 244),
        Effect.Standart.ITALIC
    ),
    Timestamp(
        Color.Converters.from_rgb(205, 214, 244),
        Effect.Standart.ITALIC
    ),
)
# fmt: on

logger = Logger(theme=theme)
