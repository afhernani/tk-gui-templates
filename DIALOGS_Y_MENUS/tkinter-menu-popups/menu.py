#!/usr/bin/python3
import tkinter as tk
try:
    from PIL import Image
except ImportError:
    print('No se pudo cargar el modulo PIL')
import os

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'menu - player'

__version__ = '0.0'


class Menupopups(tk.Menu):

    def __init__(self, parent, *args, **kargs):
        tk.Menu.__init__(self, parent, *args, **kargs)
        self.parent = parent
        self.initializeMenu()
        
    def initializeMenu(self):
        self.add_command(label="say hello", command=self.hello)
        self.add_command(label="say Goodbye", command=self.goodbye)
        self.add_separator()
        self.add_command(label="Exit", command=self.quit)

    def add_command(self, label, command):
        pass

    def hello(self):
        self.label.config(text="Hello World!!")

    def goodbye(self):
        self.label.config(text="goodbye World!!")
