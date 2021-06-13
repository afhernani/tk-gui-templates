#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, sys
import shutil
from os.path import join
from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'GUI tk - windows'
__version__ = '1'

__all__ = ('Window',)


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x120')
        self.iconbitmap('collage.ico') # pathdir
        self.title('Window copy to ...')
        # Initialize style
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('TFrame', background='green')

        # Create style for the first frame
        s.configure('Frame1.TFrame', background='red')
        # Use created style in this frame

        self.frame = ttk.Frame(self, style='Frame1.TFrame')
        # etiqueta
        # field options
        options = {'ipadx': 5, 'ipady': 5}
        # temperature label
        origen_label = ttk.Label(self.frame, text='Origen')
        origen_label.grid(column=0, row=0, sticky='W', **options)
        # origen variable and entry
        self.origen_var = tk.StringVar()
        origen_entry = ttk.Entry(self.frame, textvariable=self.origen_var)
        origen_entry.grid(column=1, row=0, columnspan=3, sticky='EW', **options)
        origen_entry.focus()
        # button select file
        origen_button = ttk.Button(self.frame, text='<...>')
        origen_button.grid(column=4, row=0, sticky='E', **options)
        origen_button.configure(command=self.origen_button_clicked)
        # result label
        self.nota_label = ttk.Label(self.frame)
        self.nota_label.grid(row=1, columnspan=4, **options)

        ttk.Button(self.frame,
                   text='Close',
                   command=self.destroy).grid(column=4, row=2, columnspan=3, **options)

        # add padding to the frame and show it
        # self.frame.grid(padx=10, pady=10, sticky='EW')
        self.frame.pack(fill=tk.BOTH, expand = True)

    def origen_button_clicked(self):
        try:
            f = self.origen_var.get()
            c = 20.14
            result = f'Original {f} = nx-{c:.2f} predic'
            self.nota_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x120')
        self.iconbitmap('collage.ico') # pathdir
        self.title('Main Window')

        # place a button on the root window
        ttk.Button(self,
                text='Open a window',
                command=self.open_window).pack(expand=True)

    def open_window(self):
        window = Window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
Aquí está la lista de posibles opciones:

column: la columna en la que se colocará el widget; 
        predeterminado 0 (columna más a la izquierda).

columnpan: cuántas columnas ocupa el widget; predeterminado 1.

ipadx, ipady: cuántos píxeles rellenar el widget, horizontal
                y verticalmente, dentro de los bordes del widget.

padx, pady : Cuántos píxeles para rellenar el widget, horizontal 
            y verticalmente, fuera de los bordes de v.

row: la fila en la que colocar el widget; por defecto la primera 
    fila que todavía está vacía.

rowpan: cuántas filas ocupa el widget; predeterminado 1.

stick: qué hacer si la celda es más grande que el widget. 
        De forma predeterminada, con sticky = '', el widget 
        está centrado en su celda. pegajoso puede ser la 
        concatenación de cadenas de cero o más de
         N, E, S, W, NE, NW, SE y SW, direcciones de la 
         brújula que indican los lados y esquinas de la 
         celda a la que se pega el widget.
"""