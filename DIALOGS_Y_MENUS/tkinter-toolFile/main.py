#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import ttk
from toolfile import *

root = Tk()
root.title('Right Click Menu')
root.iconbitmap('collage.ico') # pathdir
root.geometry("500x500")

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

# rootfile = ToolFile(root)

ttk.Button(
    root,
    text='Show an error message',
    command=lambda: ToolFile.copy(
        origen='pepe', 
        destino='juan')
    ).pack(**options)

root.mainloop()