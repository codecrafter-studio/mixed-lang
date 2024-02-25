from mixed import *
import os

try:
    def get_input() -> str | None:
        usr = input("Mixed >>>")
        return usr
except KeyboardInterrupt:
    os._exit(0)


def get_mixed(main):
    result = main_code(main)
    if result is not None:
        print(result)


try:
    while True:
        main = get_input()
        get_mixed(main)
        continue
except KeyboardInterrupt:
    os._exit(0)
