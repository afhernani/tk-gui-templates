# MENU CONTEXTUAL POPUPS

![main window](window.main.png)

![click-button-right](click-button-right.png)

[win_main](win_main.py)

```python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk
from tooltipmenu import createToolTipMenu


class App(tk.Tk):

    label: ttk.Label
    menu: tk.Menu

    def __init__(self):
        super().__init__()
        self.geometry('450x220')
        self.iconbitmap('collage.ico') # pathdir
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

```

[tooltipmenu.py](tooltipmenu.py)

```python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk
# from tkinter import ttk

__author__ = 'Hernani Aleman Ferraz'
__email__ = 'afhernani@gmail.com'
__apply__ = 'GUI tk - ToolTipMenu widget'
__version__ = '1'

__all__ = ('ToolTipMenu', 'createToolTipMenu')


class ToolTipMenu(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.menu = None
        self.x = self.y = 0

    def showtipMenu(self, menu, event):
        '''Display Menu in tooltipMenu window'''

        self.menu = menu
        if self.tipwindow or not self.menu:
            return
        menu.tk_popup(event.x_root, event.y_root)


def createToolTipMenu(widget, menu):

    toolTipMenu = ToolTipMenu(widget)

    def popup(event):
        toolTipMenu.showtipMenu(menu, event)

    widget.bind('<Button-3>', popup)

    return toolTipMenu
```

video explicativo sobre menu popups [aquí](Right_Click_Menu_Popups_With_Tkinter.mp4)