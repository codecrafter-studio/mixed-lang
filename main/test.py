import mixedgui as gui

root = gui.MWindow()
root.set_sipo((400, 400), (10, 10))
root.set_title("MWindow")

b = gui.MButton(root)
b.set_bg_fg()
b.set_text("MButton")
b.show(210, 10, 200, 100)

l = gui.MLabel(root)
l.set_text("MLabel")
l.set_bg_fg()
l.show(10, 10, 200, 100)

root.set_main()