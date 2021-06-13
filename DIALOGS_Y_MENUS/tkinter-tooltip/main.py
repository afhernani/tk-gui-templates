#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import *
from ToolTip import *

root = Tk()
root.title('Right Click Menu')
root.iconbitmap('collage.ico') # pathdir
root.geometry("500x500")

createToolTip(root, "Hola Mundo!!")

root.mainloop()