# hotpy
Python based cross-platform abbreviation hotkeys

### Installation
hotpy requires the pynut package, install it via pip:

`pip install pynput`

Clone hotpy to a local directory:

`git clone https://github.com/Akufoolz/hotpy.git`

Run `hotpy.py` to start the script

### Usage

Hotkeys are activated via the spacebar, the app will check whatever word was typed prior to hitting spacebar and if it matches an abbreviation in the `hotkeys.txt` file it will replace the word with the associcated text.

### Hotkeys File
By default the `hotkeys.txt` file should exist inside the root folder of the app. You can add new hotkeys to the file line by line, separating the hotkey abbreviation and text with double colons `::`

Example:

`expl::This is an example hotkey!`

### Config File
The config file has two variables that can be modified:

`"altDir":`

Modify this string to contain the absolute path to your `hotkeys.txt` file if you do not wish to save it within the app folder. Make sure to escape any backslashes on Windows machines.

`"hotkeyFile":`

Modify this string if you decide to name your hotkey text file different than `hotkeys.txt`