"""
SSD1306 Library for multiple font sizes
Copyright 2023-2024 . All rights reserved.
Author = Masoun Mardini
"""

import pyperclip


def Convert_TXT2BIN(font_size):
    f"""
    Convert Text font file generated in PCtoLCD2002 in binary format to save space  on pico 
    Change path in input and output file location
    File name should be always in the following format "Ascii(font_size).extension" example "Ascii24.txt"/"Ascii24.bin"
    :param font_size: 
    :return: 
    """
    with open('\\input\\Path\\to\\Ascii{}.txt'.format(font_size), 'r') as _file:
        start_chr = False
        data = []
        for _line in _file:
            """
            check for start string "!!" to skip unwanted line
            """
            if _line[-3:].rstrip() == '!!':
                start_chr = True
            if start_chr:
                for v in _line.rstrip().split(','):
                    """
                    If the value start with 0x then add it to data
                    """
                    if v.startswith('0x'):
                        # add interoperated Hex value
                        data.append(int(v, 16))

    with open('\\output\\Path\\to\\Ascii{}.bin'.format(font_size), 'wb') as _file:
        _file.write(bytearray(data))


def Printable_alphabet():
    alphabet_List = ''
    for i in range(32, 127):
        alphabet_List += ''.join(chr(i))
    pyperclip.copy(alphabet_List)

