from tkinter import filedialog
import tkinter as tk


def select_path():
    global output_path
    output_path = filedialog.askdirectory()
    return output_path


def path_to_field(master, path_entry):
    global output_path

    output_path = filedialog.askopenfilename(filetype=(('pdf', '*.pdf'), ('All Files', '*.*')))
    path_entry.set(output_path)
    master.focus_force()