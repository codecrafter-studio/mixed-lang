"""

### `Mixed` Terminal
You can use this program to get started with `Mixed` quickly (no need to package and compile, get results instantly).
How to Use:
```python
>>> <python | python3> <terminal.py> [[-m TUI | GUI] [-s /path/to/temp/file] [-l True | False] [-f /path/to/mixed/file]]
```
Other optional parameters:
`-m`: "TUI" | GUI: Specify whether to use TUI or GUI
`-l`: True | False: indicates whether to use log files
`-f`: "FilePath": Executes the selected file immediately, sending the output to the terminal

"""

import mixed
import tkinter as tk
import sys
import datetime
from tkinter import *

args = sys.argv[1:]
options = {
    '-m': 'TUI',
    '-l': False,
    '-f': ''
}

while args:
    option = args.pop(0)
    if option in options:
        options[option] = args.pop(0)

# Get Parameters
mode = options['-m']
enable_log = options['-l']
selected_file = options['-f']

def parse_code(mixed_code):
    m = mixed.Mixed(None)
    code = m.execute_mixed_command(mixed_code)
    if code:
        print(m.execute_mixed_command(code))

if enable_log:
    log = open("./log.txt", "w", encoding="utf-8")

if mode == 'TUI':
    if enable_log:
        log.write(f"{datetime.datetime.now()} - Mode Select TUI (Default)\n")
    print("Mixed Terminal\nBy CodeCrafter Studios.\n")
    while True:
        mixed_code = input("Mixed >>> ")
        parse_code(mixed_code)
elif mode == 'GUI':
    if enable_log:
        log.write(f"{datetime.datetime.now()} - Mode Select GUI\n")
    root = Tk()
    root.wm_geometry("600x400")
    root.wm_title("Mixed Terminal")
    root.config(bg="#000000")
    root.mainloop()
else:
    print(f"Unknown Mode: {mode}")

if selected_file:
    m = mixed.Mixed(selected_file)
    with open(selected_file, "r", encoding="utf-8") as f:
        code = m.execute_mixed_command(f)
        if code:
            print(m.execute_mixed_command(f))

if enable_log:
    log.close()

# print(options)
