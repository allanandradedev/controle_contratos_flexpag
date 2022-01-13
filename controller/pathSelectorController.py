from tkinter import filedialog
import tkinter as tk


def select_path(path_entry):
    global output_path

    output_path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)