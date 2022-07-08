# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""
from adafruit_hid.keyboard_layout_base import KeyboardLayoutBase


__version__ = "0.0.1-alpha.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayout(KeyboardLayoutBase):
    ASCII_TO_KEYCODE = (
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2a'  # BACKSPACE
        b'\x2b'  # '\t'
        b'\x28'  # '\n'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x29'  # ESC
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2c'  # ' '
        b'\x9e'  # '!'
        b'\x9f'  # '"'
        b'\x31'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa4'  # '&'
        b'\x34'  # "'"
        b'\xa6'  # '('
        b'\xa7'  # ')'
        b'\xa5'  # '*'
        b'\xae'  # '+'
        b'\x36'  # ','
        b'\x2d'  # '-'
        b'\x37'  # '.'
        b'\x38'  # '/'
        b'\x27'  # '0'
        b'\x1e'  # '1'
        b'\x1f'  # '2'
        b'\x20'  # '3'
        b'\x21'  # '4'
        b'\x22'  # '5'
        b'\x23'  # '6'
        b'\x24'  # '7'
        b'\x25'  # '8'
        b'\x26'  # '9'
        b'\xb3'  # ':'
        b'\x33'  # ';'
        b'\xb6'  # '<'
        b'\x2e'  # '='
        b'\xb7'  # '>'
        b'\xb8'  # '?'
        b'\xb4'  # '@'
        b'\x84'  # 'A'
        b'\x85'  # 'B'
        b'\x86'  # 'C'
        b'\x87'  # 'D'
        b'\x88'  # 'E'
        b'\x89'  # 'F'
        b'\x8a'  # 'G'
        b'\x8b'  # 'H'
        b'\x8c'  # 'I'
        b'\x8d'  # 'J'
        b'\x8e'  # 'K'
        b'\x8f'  # 'L'
        b'\x90'  # 'M'
        b'\x91'  # 'N'
        b'\x92'  # 'O'
        b'\x93'  # 'P'
        b'\x94'  # 'Q'
        b'\x95'  # 'R'
        b'\x96'  # 'S'
        b'\x97'  # 'T'
        b'\x98'  # 'U'
        b'\x99'  # 'V'
        b'\x9a'  # 'W'
        b'\x9b'  # 'X'
        b'\x9c'  # 'Y'
        b'\x9d'  # 'Z'
        b'\x2f'  # '['
        b'\x31'  # '\\'
        b'\x30'  # ']'
        b'\xa3'  # '^'
        b'\xad'  # '_'
        b'\x35'  # '`'
        b'\x04'  # 'a'
        b'\x05'  # 'b'
        b'\x06'  # 'c'
        b'\x07'  # 'd'
        b'\x08'  # 'e'
        b'\x09'  # 'f'
        b'\x0a'  # 'g'
        b'\x0b'  # 'h'
        b'\x0c'  # 'i'
        b'\x0d'  # 'j'
        b'\x0e'  # 'k'
        b'\x0f'  # 'l'
        b'\x10'  # 'm'
        b'\x11'  # 'n'
        b'\x12'  # 'o'
        b'\x13'  # 'p'
        b'\x14'  # 'q'
        b'\x15'  # 'r'
        b'\x16'  # 's'
        b'\x17'  # 't'
        b'\x18'  # 'u'
        b'\x19'  # 'v'
        b'\x1a'  # 'w'
        b'\x1b'  # 'x'
        b'\x1c'  # 'y'
        b'\x1d'  # 'z'
        b'\xaf'  # '{'
        b'\xe4'  # '|'
        b'\xb0'  # '}'
        b'\xb1'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '\\¦áéíóú€'
    HIGHER_ASCII = {
        0xa3: 0xa0,  # '£'
        0x20ac: 0x21,  # '€'
        0xe9: 0x08,  # 'é'
        0xfa: 0x18,  # 'ú'
        0xed: 0x0c,  # 'í'
        0xf3: 0x12,  # 'ó'
        0xe1: 0x04,  # 'á'
        0xac: 0xb5,  # '¬'
        0xa6: 0x35,  # '¦'
    }
    COMBINED_KEYS = {
    }