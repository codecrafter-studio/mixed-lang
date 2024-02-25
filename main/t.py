import tkinter as tk
import os
import subprocess

def run_code(event: tk.Event, entry: tk.Entry, output_entry: tk.Text, frame: tk.Frame):
    code = entry.get()
    result = subprocess.run(code, shell=True, capture_output=True, text=True)

    new_path_label = tk.Label(frame, text="Mixed >>>", fg='#ffffff', bg='#000000', font=("Consolas",))
    new_path_label.grid(row=frame.grid_size()[1], column=0, sticky='w')

    new_entry = tk.Entry(frame, fg='#ffffff', bg='#000000', bd=0, borderwidth=0, font=("Consolas",))
    new_entry.grid(row=frame.grid_size()[1], column=1, sticky='w')

    new_output_entry = tk.Text(frame, fg='#ffffff', bg='#000000', font=("Consolas",), bd=0, borderwidth=0, height=1, state='disabled', wrap='none')
    new_output_entry.grid(row=frame.grid_size()[1] + 1, column=0, columnspan=2, sticky='w')

    new_path_label.config(text="Mixed >>>")
    
    output_entry.insert("1.0", result.stdout)
    new_entry.focus_set()
    new_entry.bind("<Return>", lambda event: run_code(event, new_entry, new_output_entry, frame))

root = tk.Tk()
root.config(bg="#000000")
root.title("Terminal")
root.geometry("800x400")

frame = tk.Frame(root, bg='#000000')
frame.pack(side='top', anchor='w')

path_label = tk.Label(frame, text="Mixed >>>", fg='#ffffff', bg='#000000', font=("Consolas",))
path_label.grid(row=0, column=0, sticky='w')

entry = tk.Entry(frame, fg='#ffffff', bg='#000000', bd=0, borderwidth=0, font=("Consolas",))
entry.grid(row=0, column=1, sticky='w')

output_entry = tk.Text(frame, fg='#ffffff', bg='#000000', font=("Consolas",), bd=0, borderwidth=0)
output_entry.grid(row=1, column=0, columnspan=2, sticky='w')

entry.focus_set()
entry.bind("<Return>", lambda event: run_code(event, entry, output_entry, frame))

root.mainloop()
