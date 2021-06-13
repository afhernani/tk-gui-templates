
[Tkinter Menubutton](https://www.pythontutorial.net/tkinter/tkinter-menubutton/)
==================

**Summary**: in this tutorial, you'll learn how to use the Tkinter `Menubutton` widget.

Introduction to the `Menubutton` widget
---------------------------------------

A `Menubutton` widget is a combination of a `Button` and a `Menu` widget.

When you click the `Menubutton`, it shows a menu with choices. For example:

![](Tkinter-Menubutton-Example.png)

To create a `Menubutton` widget, you follow these steps:

First, create a `MenuButton` widget:

```python
menu_button = ttk.Menubutton(container, **options)
```

Second, create a new instance of the `Menu` class:

```python
menu = tk.Menu(menu_button, tearoff=False)Code language: Python (python)
```

Third, add one or more menu items to the menu instance. And you can add Checkbutton or Radiobutton widgets to the menu.

Finally, assign the `Menu` to the `MenuButton` instance:

```python
menu_button["menu"] = menu
```

Tkinter Menubutton widget example
---------------------------------

The following program illustrates how to use `Menubutton` widget. When you click the `MenuButton`, it'll display a menu that consists of three choices: red, green, and blue.

The background color of the main window will change based on the selected menu item of the `Menubutton`:


![](Tkinter-PanedWindow.gif)

```python

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x250')
        self.title('Menubutton Demo')

        # Menubutton variable
        self.selected_color = tk.StringVar()
        self.selected_color.trace("w", self.menu_item_selected)

        # create the menu button
        self.create_menu_button()

    def menu_item_selected(self, *args):
        """ handle menu selected event """
        self.config(bg=self.selected_color.get())

    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        colors = ('Red', 'Green', 'Blue')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Select a color')

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for color in colors:
            menu.add_radiobutton(
                label=color,
                value=color,
                variable=self.selected_color)

        # associate menu with the Menubutton
        menu_button["menu"] = menu

        menu_button.pack(expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
```

How it works.

In the `__init__()` method, we define a variable that tracks the selected value of the menu:

```python

self.selected_color = tk.StringVar()
self.selected_color.trace("w", self.menu_item_selected)
```

If the value of the `selected_color` is changed, the method menu\_item\_selected will be executed.

The `create_menu_button()` method creates the `MenuButton`:

First, create a Menubutton:

```python
menu_button = ttk.Menubutton(
    self,
    text='Select a color')
```

Then create a new menu and add three `Radiobutton` widgets derived from the `colors` tuple to the menu:

```python

# create a new menu instance
menu = tk.Menu(menu_button, tearoff=0)

for color in colors:
    menu.add_radiobutton(
        label=color,
        value=color,
        variable=self.selected_color)
```

When you select a menu item, the value of the `self.selected_color` variable changes to the value of the selected menu item.

Finally, associate menu with the `Menubutton`:

```python
menu_button["menu"] = menu
```

Summary
-------

-   Use Tkinter `Menubutton` widget to create a menu associated with a button.
