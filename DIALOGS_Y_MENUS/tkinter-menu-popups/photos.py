#!/usr/bin/python3
import tkinter as tk
try:
    from PIL import Image
except ImportError:
    print('No se pudo cargar el modulo PIL')
import os

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'photos.py - player'

__version__ = '0.0'


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Photos():
    def __init__(self):
        self._appico = tk.PhotoImage(file=resource_path('collage.png'))
        # self._logo = Image.open(resource_path('Images/flash.png'))

if __name__ == '__main__':
    root = tk.Tk()
    p = Photos()
