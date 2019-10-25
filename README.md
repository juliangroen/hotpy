# hotpy
Python based cross-platform hotkeys

### installation
hotpy requires the pynut package, install it via pip:
`pip install pynput`

clone hotpy to a local directory:
`git clone https://github.com/Akufoolz/hotpy.git`

### hotkeys file
by default the `hotkeys.txt` file should exist inside he root folder of the app. You can add new hotkeys by sepparating the hotkey abbriviation and text with double colons `::`

example:
`expl::This is an example hotkey!`

### config file
the config file has two variables that can be modified:
`"altDir":`
modify this string to contain the absolute path to your hotkeys.txt file if you do not wish to save it within the app folder. Make sure to escape any backslashes on Windows machines.
`"hotkeyFile":`
modify this string if you decide to name your hotkey text file different than hotkeys.txt