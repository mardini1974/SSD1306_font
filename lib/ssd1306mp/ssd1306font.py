"""
SSD1306 Library for multiple font sizes
Copyright 2023-2024 . All rights reserved.
Author = Masoun Mardini
"""

from .ssd1306 import *
from framebuf import *


class ssd1306font(SSD1306_I2C):
    def __init__(self, width, height, i2c):
        self.width = width
        self.height = height
        self.i2c = i2c
        self._file = None

        super().__init__(self.width, self.height, self.i2c)

    def clear(self):
        """Clear screen"""
        self.fill(0)

    def text_fb(self, string, x, y, font_size):
        """Text using frame buffer command"""
        if font_size != 8 and \
                font_size != 16 and \
                font_size != 24 and \
                font_size != 32 and \
                font_size != 40 and \
                font_size != 48 and \
                font_size != 64:
            return

        if font_size == 8:
            self.text(string, x, y)
            return
        self._display(string, x, y, font_size)

    def _get_ch(self, ch, font_size):

        if self._file is None:
            self._file = open('lib/ssd1306mp/Ascii{}.bin'.format(font_size), 'rb')
        data = self._file.read()
        # offset  = (bytes per font height * pixel per width of font) = (font_size /8) * ( font_size /2)
        offset = font_size * font_size // 16
        index = (ord(ch) - 32) * offset
        return data[index: index + offset]

    def _display(self, string, x_axis, y_axis, font_size):
        offset = 0
        for k in string:
            byte_data = self._get_ch(k, font_size)
            fb = framebuf.FrameBuffer(bytearray(byte_data), font_size // 2, font_size, framebuf.MONO_VLSB)
            self.blit(fb, x_axis + offset, y_axis)

            offset += font_size // 2
