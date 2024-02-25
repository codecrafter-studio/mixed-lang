import tkinter as tk
import tkinter.ttk as ttk
import os
import inspect

__filename__ = os.path.abspath(inspect.getframeinfo(inspect.stack()[-1][0])[0])


class MWindow(tk.Tk):

    """Developed By tkinter.Tk"""

    def __init__(self) -> None:
        super().__init__()
        self.set_title()
        self.set_sipo((400, 400), (20, 20))

    def set_sipo(self, size: tuple[400, 400], position: tuple[20, 20]):
        return self.wm_geometry(f"{size[0]}x{size[1]}+{position[0]}+{position[1]}")

    def set_title(self, title: str = "MixedWindow"):
        return self.wm_title(title)

    def set_attributes(self, __option, __vaule, /, *args):
        return self.wm_attributes(__option, __vaule, *args)

    def set_protocol(self, name, func):
        return self.wm_protocol(name, func)

    def set_main(self, n: int = 0):
        return self.mainloop(n)


class MTopWindow(tk.Toplevel):

    """Developed By tkinter.Toplevel"""

    def __init__(self) -> None:
        super().__init__()
        self.set_title()
        self.set_sipo((400, 400), (20, 20))

    def set_sipo(self, size: tuple[400, 400], position: tuple[20, 20]):
        return self.wm_geometry(f"{size[0]}x{size[1]}+{position[0]}+{position[1]}")

    def set_title(self, title: str = "MixedWindow"):
        return self.wm_title(title)

    def set_attributes(self, __option, __vaule, /, *args):
        return self.wm_attributes(__option, __vaule, *args)

    def set_protocol(self, name, func):
        return self.wm_protocol(name, func)

    def set_main(self, n: int = 0):
        return self.mainloop(n)


class MLabel(tk.Label):

    """Developed By tkinter.Label"""

    def __init__(self, master: tk.Misc | None = None) -> None:
        super().__init__(master)
        self.set_bg_fg()

    def set_text(self, text: str | int | bytes | None) -> str | int | bytes | None:
        self['text'] = text
        return text

    def set_bg_fg(self, bg: str = "white", fg: str = "black") -> str:
        self['bg'], self['fg'] = bg, fg
        return bg, fg

    def show(self, x: int, y: int, width: int, height: int):
        return self.place(x=x, y=y, width=width, height=height)

    def set_x(self, x: int):
        return self.place(x=x)

    def set_y(self, y: int):
        return self.place(y=y)

    def set_width(self, width: int):
        return self.place(width=width)

    def set_height(self, height: int):
        return self.place(height=height)


class MButton(tk.Button):

    """Developed By tkinter.Button"""

    def __init__(self, master: tk.Misc | None = None) -> None:
        super().__init__(master)
        self.set_bg_fg()

    def set_text(self, text: str | int | bytes | None) -> str | int | bytes | None:
        self['text'] = text
        return text

    def set_bg_fg(self, bg: str = "white", fg: str = "black") -> str:
        self['bg'], self['fg'] = bg, fg
        return bg, fg

    def show(self, x: int, y: int, width: int, height: int):
        return self.place(x=x, y=y, width=width, height=height)

    def set_x(self, x: int):
        return self.place(x=x)

    def set_y(self, y: int):
        return self.place(y=y)

    def set_width(self, width: int):
        return self.place(width=width)

    def set_height(self, height: int):
        return self.place(height=height)
