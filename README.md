# hotpy
Python based cross-platform abbreviation hotkeys

## TODO
- Symbols in hotkey abbreviations.
- Alert, prompt, and confirm functions for complex hotkey output.

## Installation
hotpy requires the pynut package, install it via pip:

`pip install pynput`

Clone hotpy to a local directory:

`git clone https://github.com/Akufoolz/hotpy.git`

Run `hotpy.py` to start the script

## Usage

Hotkeys are activated via the spacebar. The string of characters typed prior to hitting spacebar is compared to the list of abbreviations from the `hotkeys.txt` file. If a match is found the hotkey text will replace the abbreviation.

## Hotkeys File
Hotkeys are defined within the `hotkeys.txt` file. Create a new text file called `hotkeys.txt` inside the root folder of the app.

#### Single Line Hotkeys
 To add a single line hotkey to the `hotkeys.txt` file. Separate the hotkey abbreviation and text with double colons `::`

Example:

```
expl::This is an example hotkey!
```

#### Multi-Line Hotkeys
 To add a multi-line hotkey to the `hotkeys.txt` file. Use the `:(` marker at the end of the hotkey abbreviation. Place your multi-line text line by line beneath the abbreviation line. End the hotkey by placing a `):` marker on it's own line beneath the text lines.

Example:

```
exml:(
The text of this
hotkey is on
multiple lines.
):
```

## Config File
The config file has two key values that can be modified:

```
"altDir": ""
```

Modify this key's value to contain the absolute path to your `hotkeys.txt` file if you do not wish to save it within the root of app folder. Make sure to escape any backslashes on Windows machines.

```
"hotkeyFile": "hotkeys.txt"
```

Modify this key's value if you decide to name your hotkey text file different than `hotkeys.txt`