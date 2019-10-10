import pyautogui
from pynput.keyboard import Controller, Key, KeyCode, Listener

def exampleFunction():
    pyautogui.alert("example alert!")

hotkeys = {
    "expl": "Example",
    "exfun": exampleFunction
    }