from tkinter import *


class PlaceHolderEntry(Entry):
    def __init__(self, master=None, placeholder = 'PLACEHOLDER', color='gray', bd=None, type= None, bg=None,
                 highlightthickness=None, default_fg_color = None, font: tuple = ('Roboto', 11), state=None):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = default_fg_color
        self['state'] = state
        self.bind('<FocusIn>', self.foc_in)
        self.bind('<FocusOut>', self.foc_out)
        self['font'] = font
        self['bg'] = bg
        self['bd'] = bd
        self['highlightthickness'] = highlightthickness
        self.type = type

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            if self.type == 'password':
                self['show'] = '*'
            self.delete('0', END)
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self['show'] = ''
            self.put_placeholder()
