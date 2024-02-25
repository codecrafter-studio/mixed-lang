"""

### `Mixed` Terminal
You can use this program to get started with `Mixed` quickly (no need to package and compile, get results instantly).
How to Use:
```python
>>> <python | python3> <terminal.py> [[-m TUI | GUI] [-s /path/to/temp/file] [-l True | False] [-f /path/to/mixed/file]]
```
Other optional parameters:
`-m`: "TUI" | GUI: Specify whether to use TUI or GUI
`-s`: "FilePath": the path where the cached file is saved
`-l`: True | False: indicates whether to use log files
`-f`: "FilePath": Executes the selected file immediately, sending the output to the terminal

"""

import mixed
import tkinter as tk
import sys

args = sys.argv[1:]
options = {
    '-m': 'TUI',
    '-s': '',
    '-l': 'False',
    '-f': ''
}

while args:
    option = args.pop(0)
    if option in options:
        options[option] = args.pop(0)

# Get Parameters
# print("Options:")
# for key, value in options.items():
#     print(f"{key}: {value}")

mode = options['-m']
cache_file_path = options['-s']
enable_log = options['-l']
selected_file = options['-f']

if mode == 'TUI':
    print("Mode Select TUI (Default)")
elif mode == 'GUI':
    print("Mode Select GUI")
    ...

if selected_file:
    m = mixed.Mixed(selected_file)
    with open(selected_file, "r", encoding="utf-8") as f:
        m.execute_mixed_code(f)
