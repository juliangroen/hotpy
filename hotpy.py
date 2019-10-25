#TODO
# 1. hotkey abbreviations with special chars
import os, sys, json
from pynput.keyboard import Controller, Key, KeyCode, Listener

keyboard = Controller()
combo = set()
keys = []

def getConfigFile():

    pwd = os.path.dirname(sys.argv[0])
    pathFile = os.path.join(pwd, "config.json")

    with open(pathFile, 'r') as f:
        cfg = json.load(f)

    return cfg

def getHotkeysFromFile():

    cfg = getConfigFile()

    if not cfg["altDir"]:
        pwd = os.path.dirname(sys.argv[0])
        pathFile = os.path.join(pwd, cfg["hotkeyFile"]) 
    else:
        pwd = os.path.dirname(cfg["altDir"])
        pathFile = os.path.join(pwd, cfg["hotkeyFile"]) 

    with open(pathFile) as hkFile:
        hks = dict(line.strip().split("::", 1) for line in hkFile)

    return hks

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

    cfg = getConfigFile()

    if (set([str(x)[4:] for x in combo]) == set(cfg["exitCombo"].split(", ")) or
        set([str(x)[4:] for x in combo]) == set(cfg["macExitCombo"].split(", "))):
        print("exiting...")
        return False

    if key in combo:
        combo.remove(key)

def checkForHotkey():

    hk = "".join(keys)
    match = getHotkeysFromFile().get(hk)

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
    
    keys.clear()

def exitComboPrint():

    if sys.platform == "win32":
        print("Press {} together to exit.".format(getConfigFile()["exitCombo"]))
    elif sys.platform == "darwin":
        print("Press {} together to exit.".format(getConfigFile()["macExitCombo"]))

def main():

    exitComboPrint()
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()