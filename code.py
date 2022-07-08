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

defaultDelay = 0

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# turn off automatically reloading when files are written to the pico
supervisor.disable_autoreload()

time.sleep(.5)

duckyCommands = {
    'WINDOWS': Keycode.WINDOWS, 'GUI': Keycode.GUI,
    'APP': Keycode.APPLICATION, 'MENU': Keycode.APPLICATION, 'SHIFT': Keycode.SHIFT,
    'ALT': Keycode.ALT, 'CONTROL': Keycode.CONTROL, 'CTRL': Keycode.CONTROL,
    'DOWNARROW': Keycode.DOWN_ARROW, 'DOWN': Keycode.DOWN_ARROW, 'LEFTARROW': Keycode.LEFT_ARROW,
    'LEFT': Keycode.LEFT_ARROW, 'RIGHTARROW': Keycode.RIGHT_ARROW, 'RIGHT': Keycode.RIGHT_ARROW,
    'UPARROW': Keycode.UP_ARROW, 'UP': Keycode.UP_ARROW, 'BREAK': Keycode.PAUSE,
    'PAUSE': Keycode.PAUSE, 'CAPSLOCK': Keycode.CAPS_LOCK, 'DELETE': Keycode.DELETE,
    'END': Keycode.END, 'ESC': Keycode.ESCAPE, 'ESCAPE': Keycode.ESCAPE, 'HOME': Keycode.HOME,
    'INSERT': Keycode.INSERT, 'NUMLOCK': Keycode.KEYPAD_NUMLOCK, 'PAGEUP': Keycode.PAGE_UP,
    'PAGEDOWN': Keycode.PAGE_DOWN, 'PRINTSCREEN': Keycode.PRINT_SCREEN, 'ENTER': Keycode.ENTER,
    'SCROLLLOCK': Keycode.SCROLL_LOCK, 'SPACE': Keycode.SPACE, 'TAB': Keycode.TAB,
    'BACKSPACE': Keycode.BACKSPACE,
    'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C, 'D': Keycode.D, 'E': Keycode.E,
    'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H, 'I': Keycode.I, 'J': Keycode.J,
    'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M, 'N': Keycode.N, 'O': Keycode.O,
    'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R, 'S': Keycode.S, 'T': Keycode.T,
    'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W, 'X': Keycode.X, 'Y': Keycode.Y,
    'Z': Keycode.Z, 'F1': Keycode.F1, 'F2': Keycode.F2, 'F3': Keycode.F3,
    'F4': Keycode.F4, 'F5': Keycode.F5, 'F6': Keycode.F6, 'F7': Keycode.F7,
    'F8': Keycode.F8, 'F9': Keycode.F9, 'F10': Keycode.F10, 'F11': Keycode.F11,
    'F12': Keycode.F12,

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
        if(led.value == True):
            led.value = False
        else:
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


def getKeyStatus(keynum):
    if (keynum == 0):
        keyStatusPin = digitalio.DigitalInOut(GP0)
        keyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
        keyStatus = not keyStatusPin.value
        return(keyStatus)
    if (keynum == 1):
        keyStatusPin = digitalio.DigitalInOut(GP1)
        keyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
        keyStatus = not keyStatusPin.value
        return(keyStatus)
    if (keynum == 2):
        keyStatusPin = digitalio.DigitalInOut(GP2)
        keyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
        keyStatus = not keyStatusPin.value
        return(keyStatus)
    if (keynum == 3):
        keyStatusPin = digitalio.DigitalInOut(GP3)
        keyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
        keyStatus = not keyStatusPin.value
        return(keyStatus)
    if (keynum == 4):
        keyStatusPin = digitalio.DigitalInOut(GP4)
        keyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
        keyStatus = not keyStatusPin.value
        return(keyStatus)
    return(False)


def getSwitchStatus():
    switchStatusDownPin = digitalio.DigitalInOut(GP6)
    switchStatusDownPin.switch_to_input(pull=digitalio.Pull.UP)
    switchStatusDown = not switchStatusDownPin.value

    switchStatusUpPin = digitalio.DigitalInOut(GP6)
    switchStatusUpPin.switch_to_input(pull=digitalio.Pull.UP)
    switchStatusUp = not switchStatusUpPin.value
    if (not (switchStatusDown and switchStatusUp)):
        return(2)
    if (switchStatusDown):
        return(3)
    if (switchStatusUp):
        return(1)


def selectPayload():
    keystatus1 = getKeyStatus(0)
    keystatus2 = getKeyStatus(1)
    keystatus3 = getKeyStatus(2)
    keystatus4 = getKeyStatus(3)
    keystatus5 = getKeyStatus(4)
    mode = getSwitchStatus()
    if (mode == 1):
        if(keystatus1 == True):
            payload = "key1a.dd"
        elif(keystatus2 == True):
            payload = "key2a.dd"
        elif(keystatus3 == True):
            payload = "key3a.dd"
        elif(keystatus4 == True):
            payload = "key4a.dd"
        elif(keystatus5 == True):
            payload = "key5a.dd"
        else:
            return False
    if (mode == 2):
        return False
    if (mode == 3):
        if(keystatus1 == True):
            payload = "key1b.dd"
        elif(keystatus2 == True):
            payload = "key2b.dd"
        elif(keystatus3 == True):
            payload = "key3b.dd"
        elif(keystatus4 == True):
            payload = "key4b.dd"
        elif(keystatus5 == True):
            payload = "key5b.dd"
        else:
            return False
    return payload


runScript("key1a.dd")

while True:
    payload = selectPayload()
    if (payload != False):
        runScript(payload)
