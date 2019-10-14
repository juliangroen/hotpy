#TODO
# 1. hotkey abbreviations with special chars

from hotkeys import hotkeys
from pynput.keyboard import Controller, Key, KeyCode, Listener

keyboard = Controller()
exitHotkey = {Key.ctrl_l, Key.shift, Key.alt_l, Key.esc}
combo = set()
keys = []

def on_press(key):
    try:
        keys.append(str(key.char))
    except AttributeError:
        pass

    if key not in combo:
        combo.add(key)

    if key == Key.space:
        checkForHotkey()
        keys.clear()

    if key == Key.backspace:
        if keys:
            keys.pop()
    
def on_release(key):
    if combo == exitHotkey:
        print("exiting...")
        return False

    if key in combo:
        combo.remove(key)

def checkForHotkey():
    hk = "".join(keys)
    match = hotkeys.get(hk)

    if match: 
        for i in range(len(keys) + 1):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        if callable(match):
            match() 
        elif isinstance(match, str):
            keyboard.type(match)
        print("matched {0} hotkey!".format(hk))

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()