#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# import os
# import sys
# import shutil
# from os.path import join
# from functools import partial
import tkinter as tk
from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showerror, showinfo
# import threading
from tooltipmenu import createToolTipMenu
from photos import Photos
import os

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'win_main'

__version__ = '0.0'


class App(tk.Tk):

    label: ttk.Label
    menu: tk.Menu

    def __init__(self):
        super().__init__()
        self.geometry('450x220')
        self.ph = Photos()
        self.wm_iconphoto(True, self.ph._appico)
        if os.name == 'nt':
            self.wm_iconbitmap(bitmap='collage.ico')
        else:
            self.wm_iconbitmap(bitmap='@collage.xbm')
        self.title('Windows xample popups menu')
        self.initialize()
        self.bind('<Button-3>', self.my_popup)

    def initialize(self):
        # etiqueta.
        self.label = ttk.Label(self, text="", font=("Helvetica", 30))
        self.label.pack(pady=20)
        self.initializeMenu()

    def initializeMenu(self):
        self.menu = tk.Menu(self, tearoff=False)  # linea punteada apagada.
        self.menu.add_command(label="say hello", command=self.hello)
        self.menu.add_command(label="say Goodbye", command=self.goodbye)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.quit)

        createToolTipMenu(self, self.menu)

    def hello(self):
        self.label.config(text="Hello World!!")

    def goodbye(self):
        self.label.config(text="goodbye World!!")

    def my_popup(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)


if __name__ == "__main__":
    app = App()
    app.mainloop()
