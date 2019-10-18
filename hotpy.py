#TODO
# 1. hotkey abbreviations with special chars

from hotkeys import hotkeys
from pynput.keyboard import Controller, Key, KeyCode, Listener

keyboard = Controller()
exitHotkey = {Key.ctrl_l, Key.shift, Key.alt_l, Key.esc}
combo = set()
keys = []

def getHotkeysFromFile():
    with open("./hotkeys.txt") as hkFile:
        hks = dict(line.strip().split(": ", 1) for line in hkFile)
    return hks

hkDict = getHotkeysFromFile()

def on_press(key):

    try:
        keys.append(key.char)
    except AttributeError:
        pass

    if key == Key.space or key == Key.enter:
        checkForHotkey()

    if key == Key.backspace:
        if keys:
            keys.pop()

    if key not in combo:
        combo.add(key)
    
def on_release(key):
    if combo == exitHotkey:
        print("exiting...")
        return False

    if key in combo:
        combo.remove(key)

def checkForHotkey():
    hk = "".join(keys)
    #match = hotkeys.get(hk)
    match = hkDict.get(hk)

    if match: 
        for _ in range(len(keys) + 1):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        if callable(match):
            match() 
        elif isinstance(match, str):
            keyboard.type(match)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        print("matched {0} hotkey!".format(hk))

    print(hk)
    keys.clear()

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
