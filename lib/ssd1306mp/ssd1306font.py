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
        self.data = {}
        super().__init__(self.width, self.height, self.i2c)

    def clear(self):
        """Clear screen"""
        self.fill(0)

    def text_fb(self, string, x, y, fontname):
        """Text using frame buffer command"""
        
        self.load_font(fontname=fontname)
        self._display(string, x, y, font_size)

    def _get_ch(self, ch, font_size):
        offset = font_size * font_size // 16
        index = (ord(ch) - 32) * offset
        return self.data["{}".format(font_size)][index: index + offset]

    def load_font(self, fontname = 'lib/ssd1306mp/Ascii16.bin'):
        if not fontname in self.data:
            with open(fontname, 'rb') as file:
                self.data[fontname] = file.read()

    def _display(self, string, x_axis, y_axis, font_size):
        offset = 0
        for k in string:
            byte_data = self._get_ch(k, font_size)
            fb = framebuf.FrameBuffer(bytearray(byte_data), font_size // 2, font_size, framebuf.MONO_VLSB)
            self.blit(fb, x_axis + offset, y_axis)

            offset += font_size // 2
