import pyautogui
from pynput.keyboard import Controller, Key, KeyCode, Listener

def testFunction():
    print("Yay!")
    pyautogui.alert("test alert!")

hotkeys = {
    "j.g": "julian.groen",
    "jsg": "Julian Groen",
    #"jg@wgu": "julian.groen@wgu.edu",
    "tyfe": "This is Julian from the IT Site Support team.",
    "wgup": "877-435-7948",
    "sshe": "I am shipping you a XequipTextX via FedEx, please feel free to track the package via the following link:",
    "spue": "Please feel free to stop by the Site Support front desk to pick up %pickupText% at your earliest convenience.",
    "srtle": "I have included a return shipping label in the package, please ship your current laptop back to us within 5 business days from receiving your replacement laptop.",
    "srtlle": "I have included a return shipping label in the package, please ship your current laptop back to us as soon as possible so we may migrate your data to a replacement laptop.",
    "sode": "Please ensure that all your files and folders are synced via Microsoft OneDrive prior to switching laptops.",
    "scte": "I am going to close this ticket at this time. I will follow-up with you regarding return of your current laptop via a separate ticket if needed.",
    "tfun": testFunction
    }