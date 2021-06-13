#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, sys
import shutil
from os.path import join
from functools import partial
import tkinter as tk
# from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'GUI tk - ToolFile widget'
__version__ = '1'

__all__ = ('ToolFile',)


class ToolFile(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    @staticmethod
    def copy(origen, destino, *args):
        try:
            shutil.copy(origen, destino)
        except IOError as e:
            showerror(title="Error al copiar",
                      message='Don`t panic!. ' +
                              str(e.args) +
                              origen
                      )

    @staticmethod
    def move(origen, destino, *args):
        try:
            shutil.move(origen, destino)
        except IOError as e:
            showerror(title="Error to move",
                      message='Don`t panic!. ' +
                              str(e.args) +
                              origen
                      )

    @staticmethod
    def remove(origen, *args):
        try:
            os.remove(origen)
        except IOError as e:
            showerror(title="Error to remove",
                      message='Don`t panic!. ' +
                              str(e.args) +
                              origen
                      )
