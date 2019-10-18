import pyautogui
from pynput.keyboard import Controller, Key, KeyCode, Listener

def exampleFunction():
    pyautogui.alert("example alert!")

hotkeys = {
    "expl": "This is an example hotkey.",
    "exfun": exampleFunction
    }