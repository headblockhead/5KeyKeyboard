import usb_hid
from adafruit_hid.keyboard import Keyboard

# https://www.neradoc.me/layouts/
# https://kbdlayout.info/kbduk
# https://github.com/Neradoc/Circuitpython_Keyboard_Layouts

from adafruit_hid.keyboard_layout_win_uk import KeyboardLayout
from adafruit_hid.keycode_win_uk import Keycode

import supervisor

import time
import digitalio
from board import *
import pwmio
import board

defaultDelay = 0

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# turn off automatically reloading when files are written to the pico
supervisor.disable_autoreload()

time.sleep(.5)

duckyCommands = {
    'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C, 'D': Keycode.D, 'E': Keycode.E, 'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H, 'I': Keycode.I, 'J': Keycode.J, 'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M, 'N': Keycode.N, 'O': Keycode.O, 'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R, 'S': Keycode.S, 'T': Keycode.T, 'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W, 'X': Keycode.X, 'Y': Keycode.Y, 'Z': Keycode.Z, '1': Keycode.ONE, '2': Keycode.TWO, '3': Keycode.THREE, '4': Keycode.FOUR, '5': Keycode.FIVE, '6': Keycode.SIX, '7': Keycode.SEVEN, '8': Keycode.EIGHT, '9': Keycode.NINE, '0': Keycode.ZERO, 'ENTER': Keycode.ENTER, 'RETURN': Keycode.RETURN, 'ESCAPE': Keycode.ESCAPE, 'BACKSPACE': Keycode.BACKSPACE, 'TAB': Keycode.TAB, 'SPACEBAR': Keycode.SPACEBAR, 'SPACE': Keycode.SPACE, 'MINUS': Keycode.MINUS, 'EQUALS': Keycode.EQUALS, 'LEFT_BRACKET': Keycode.LEFT_BRACKET, 'RIGHT_BRACKET': Keycode.RIGHT_BRACKET, 'BACKSLASH': Keycode.BACKSLASH, 'POUND': Keycode.POUND, 'SEMICOLON': Keycode.SEMICOLON, 'QUOTE': Keycode.QUOTE, 'GRAVE_ACCENT': Keycode.GRAVE_ACCENT, 'COMMA': Keycode.COMMA, 'PERIOD': Keycode.PERIOD, 'FORWARD_SLASH': Keycode.FORWARD_SLASH, 'CAPS_LOCK': Keycode.CAPS_LOCK, 'F1': Keycode.F1, 'F2': Keycode.F2, 'F3': Keycode.F3, 'F4': Keycode.F4, 'F5': Keycode.F5, 'F6': Keycode.F6, 'F7': Keycode.F7, 'F8': Keycode.F8, 'F9': Keycode.F9, 'F10': Keycode.F10, 'F11': Keycode.F11, 'F12': Keycode.F12, 'PRINT_SCREEN': Keycode.PRINT_SCREEN, 'SCROLL_LOCK': Keycode.SCROLL_LOCK, 'PAUSE': Keycode.PAUSE, 'INSERT': Keycode.INSERT, 'HOME': Keycode.HOME, 'PAGE_UP': Keycode.PAGE_UP, 'DELETE': Keycode.DELETE, 'END': Keycode.END, 'PAGE_DOWN': Keycode.PAGE_DOWN, 'RIGHT_ARROW': Keycode.RIGHT_ARROW, 'LEFT_ARROW': Keycode.LEFT_ARROW, 'DOWN_ARROW': Keycode.DOWN_ARROW, 'UP_ARROW': Keycode.UP_ARROW, 'KEYPAD_NUMLOCK': Keycode.KEYPAD_NUMLOCK, 'KEYPAD_FORWARD_SLASH': Keycode.KEYPAD_FORWARD_SLASH, 'KEYPAD_ASTERISK': Keycode.KEYPAD_ASTERISK, 'KEYPAD_MINUS': Keycode.KEYPAD_MINUS, 'KEYPAD_PLUS': Keycode.KEYPAD_PLUS, 'KEYPAD_ENTER': Keycode.KEYPAD_ENTER, 'KEYPAD_ONE': Keycode.KEYPAD_ONE, 'KEYPAD_TWO': Keycode.KEYPAD_TWO, 'KEYPAD_THREE': Keycode.KEYPAD_THREE, 'KEYPAD_FOUR': Keycode.KEYPAD_FOUR, 'KEYPAD_FIVE': Keycode.KEYPAD_FIVE, 'KEYPAD_SIX': Keycode.KEYPAD_SIX, 'KEYPAD_SEVEN': Keycode.KEYPAD_SEVEN, 'KEYPAD_EIGHT': Keycode.KEYPAD_EIGHT, 'KEYPAD_NINE': Keycode.KEYPAD_NINE, 'KEYPAD_ZERO': Keycode.KEYPAD_ZERO, 'KEYPAD_PERIOD': Keycode.KEYPAD_PERIOD, 'KEYPAD_BACKSLASH': Keycode.KEYPAD_BACKSLASH, 'APPLICATION': Keycode.APPLICATION, 'POWER': Keycode.POWER, 'KEYPAD_EQUALS': Keycode.KEYPAD_EQUALS, 'F13': Keycode.F13, 'F14': Keycode.F14, 'F15': Keycode.F15, 'F16': Keycode.F16, 'F17': Keycode.F17, 'F18': Keycode.F18, 'F19': Keycode.F19, 'F20': Keycode.F20, 'F21': Keycode.F21, 'F22': Keycode.F22, 'F23': Keycode.F23, 'F24': Keycode.F24, 'LEFT_SHIFT': Keycode.LEFT_SHIFT, 'LEFT_ALT': Keycode.LEFT_ALT, 'RIGHT_GUI': Keycode.LEFT_GUI, 'RIGHT_CONTROL': Keycode.RIGHT_CONTROL, 'RIGHT_SHIFT': Keycode.RIGHT_SHIFT, 'RIGHT_ALT': Keycode.RIGHT_ALT, 'RIGHT_GUI': Keycode.RIGHT_GUI, 'LEFT_CONTROL': Keycode.LEFT_CONTROL, 'CTRL': Keycode.CONTROL, 'CONTROL': Keycode.CONTROL, "COMMAND": Keycode.COMMAND, "WINDOWS": Keycode.WINDOWS, "WIN": Keycode.WINDOWS, "OPTION": Keycode.ALT, "ALT": Keycode.ALT, "SHIFT": Keycode.SHIFT, "SPACE": Keycode.SPACE, "RETURN": Keycode.RETURN

}


def convertLine(line):
    newline = []
    # print(line)
    # loop on each key - the filter removes empty values
    for key in filter(None, line.split(" ")):
        key = key.upper()
        # find the keycode for the command in the list
        command_keycode = duckyCommands.get(key, None)
        if command_keycode is not None:
            # if it exists in the list, use it
            newline.append(command_keycode)
        elif hasattr(Keycode, key):
            # if it's in the Keycode module, use it (allows any valid keycode)
            newline.append(getattr(Keycode, key))
        else:
            # if it's not a known key name, show the error for diagnosis
            print(f"Unknown key: <{key}>")
    # print(newline)
    return newline


def runScriptLine(line):
    for k in line:
        kbd.press(k)
    kbd.release_all()


def sendString(line):
    layout.write(line)


def parseLine(line):
    global defaultDelay
    if(line[0:3] == "REM"):
        # ignore ducky script comments
        pass
    elif(line[0:5] == "DELAY"):
        time.sleep(float(line[6:]) / 1000)
    elif(line[0:6] == "STRING"):
        sendString(line[7:])
    elif(line[0:5] == "PRINT"):
        print("[SCRIPT]: " + line[6:])
    elif(line[0:6] == "IMPORT"):
        runScript(line[7:])
    elif(line[0:13] == "DEFAULT_DELAY"):
        defaultDelay = int(line[14:]) * 10
    elif(line[0:12] == "DEFAULTDELAY"):
        defaultDelay = int(line[13:]) * 10
    elif(line[0:3] == "LED"):
        if (line[4:6] == "on"):
            led.value = False
        elif (line[4:7] == "off"):
            led.value = True
    else:
        newScriptLine = convertLine(line)
        runScriptLine(newScriptLine)


def runScript(file):
    global defaultDelay

    duckyScriptPath = file
    try:
        f = open(duckyScriptPath, "r", encoding='utf-8')
        previousLine = ""
        for line in f:
            line = line.rstrip()
            if(line[0:6] == "REPEAT"):
                for i in range(int(line[7:])):
                    # repeat the last command
                    parseLine(previousLine)
                    time.sleep(float(defaultDelay) / 1000)
            else:
                parseLine(line)
                previousLine = line
            time.sleep(float(defaultDelay) / 1000)
    except OSError as e:
        print("Unable to open file ", file)


KeyPin0 = digitalio.DigitalInOut(GP0)
KeyPin0.switch_to_input(pull=digitalio.Pull.DOWN)

KeyPin1 = digitalio.DigitalInOut(GP1)
KeyPin1.switch_to_input(pull=digitalio.Pull.DOWN)

KeyPin2 = digitalio.DigitalInOut(GP2)
KeyPin2.switch_to_input(pull=digitalio.Pull.DOWN)

KeyPin3 = digitalio.DigitalInOut(GP3)
KeyPin3.switch_to_input(pull=digitalio.Pull.DOWN)

KeyPin4 = digitalio.DigitalInOut(GP4)
KeyPin4.switch_to_input(pull=digitalio.Pull.DOWN)


def getKeyStatus(keynum):
    if (keynum == 0):
        keyStatus = KeyPin0.value
        return(keyStatus)
    if (keynum == 1):
        keyStatus = KeyPin1.value
        return(keyStatus)
    if (keynum == 2):
        keyStatus = KeyPin2.value
        return(keyStatus)
    if (keynum == 3):
        keyStatus = KeyPin3.value
        return(keyStatus)
    if (keynum == 4):
        keyStatus = KeyPin4.value
        return(keyStatus)
    return(False)


def selectPayload():
    keystatus1 = getKeyStatus(0)
    keystatus2 = getKeyStatus(1)
    keystatus3 = getKeyStatus(2)
    keystatus4 = getKeyStatus(3)
    keystatus5 = getKeyStatus(4)

    if(keystatus1 == True):
        payload = "button5.dd"
    elif(keystatus2 == True):
        payload = "button4.dd"
    elif(keystatus3 == True):
        payload = "button3.dd"
    elif(keystatus4 == True):
        payload = "button2.dd"
    elif(keystatus5 == True):
        payload = "button1.dd"
    else:
        return False
    return payload


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# runScript("button1.dd")
while True:
    payload = selectPayload()
    if (payload != False):
        runScript(payload)
