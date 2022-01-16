from tkinter import filedialog
import tkinter as tk


def select_path():
    global output_path
    output_path = filedialog.askdirectory()
    return output_path