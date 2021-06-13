#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import time
from tkinter import ttk
import tkinter as tk
import threading
from tkinter.messagebox import showinfo

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'GUI tk - Progresswin'
__version__ = '1'

__all__ = ('Progresswin', 'Progressthreadwin')


class Progressthreadwin(tk.Toplevel):

    pb: ttk.Progressbar
    foo_thread: threading

    def __init__(self, parent, **options):
        super(Progressthreadwin, self).__init__(parent, **options)
        self.grid()
        self.geometry('300x60')
        # self.iconbitmap('collage.ico')  # pathdir
        if "nt" == os.name:
            self.wm_iconbitmap(bitmap="collage.ico")
        else:
            self.wm_iconbitmap(bitmap="@collage.xbm")
        self.title('PROGRESS ...')
        self.wm_transient(parent)  # desiconizable

        # progressbar
        self.pb = ttk.Progressbar(self, orient='horizontal',
                                  mode='determinate', length=280)
        # place the progressbar
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

    def assing_thread(self, target, *args):
        self.foo_thread = threading.Thread(target=target, args=args)

    def start(self):
        if hasattr(self, 'foo_thread'):
            self.foo_thread.daemon = True
            self.pb.start()
            self.foo_thread.start()
            self.after(20, self.check_foo_thread)
        else:
            print('No se ha asignado la tarea')

    def check_foo_thread(self):
        if self.foo_thread.is_alive():
            self.after(20, self.check_foo_thread)
        else:
            self.pb.stop()
            self.destroy()


class Progresswin(tk.Toplevel):

    pb: ttk.Progressbar

    def __init__(self, parent, **options):
        super(Progresswin, self).__init__(parent, **options)
        self.grid()
        self.geometry('310x120')
        # self.iconbitmap('collage.ico')  # pathdir
        if "nt" == os.name:
            self.wm_iconbitmap(bitmap="collage.ico")
        else:
            self.wm_iconbitmap(bitmap="@collage.xbm")
        self.title('PROGRESS ...')

        # progressbar
        self.pb = ttk.Progressbar(self, orient='horizontal',
                                  mode='determinate', length=280 )
        # place the progressbar
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

        # label
        self.value_label = ttk.Label(self, text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)

        # start button
        self.start_button = ttk.Button(self, text='Progress', command=self.progress )
        self.start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

    def update_progress_label(self):
        return f"Current Progress: {self.pb['value']}%"

    def progress(self):
        self.pb.start()
        self.pb.after(10, self.process)

    def process(self):
        if self.pb['value'] < 99.0:
            self.value_label['text'] = self.update_progress_label()
            self.pb.after(10, self.process)
        else:
            # showinfo(message='The progress completed!')
            self.pb.stop()
            # self.destroy()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x120')

        # self.iconbitmap('collage.ico')  # pathdir
        # img = tk.PhotoImage(file='collage.png')
        # self.tk.call('wm', 'iconphoto', self._w, img)

        if "nt" == os.name:
            self.wm_iconbitmap(bitmap="collage.ico")
        else:
            self.wm_iconbitmap(bitmap="@collage.xbm")

        self.title('Progress bar at Window')

        # place a button on the root window
        ttk.Button(self,
                text='Window progress ...',
                command=self.win_progress).pack(expand=True)

        ttk.Button(self,
                   text='Window progress thread ...',
                   command=self.win_thread).pack(expand=True)

    def win_progress(self):

        window = Progresswin(self)
        # window.file.set("E:\\Imagenes\\coronavirus.jfif")
        # window.name.set("Nevo nombre")
        window.grab_set()

    def win_thread(self):

        window = Progressthreadwin(self)
        # window.file.set("E:\\Imagenes\\coronavirus.jfif")
        # window.name.set("Nevo nombre")
        window.assing_thread(self.foo)
        window.start()
        window.grab_set()

    @staticmethod
    def foo():
        import time
        time.sleep(3)


if __name__ == "__main__":
    app = App()
    app.mainloop()
