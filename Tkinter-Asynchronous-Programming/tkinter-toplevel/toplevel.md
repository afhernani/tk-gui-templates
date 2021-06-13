
Tkinter Toplevel
================

**Summary**: in this tutorial, you'll learn how to create multiple windows in a Tkinter application using the Tkinter Toplevel class.

Introduction to Tkinter Toplevel window
---------------------------------------

In a Tkinter application, the instance of the `Tk` class represents the [main window](https://www.pythontutorial.net/tkinter/tkinter-window/).

When you destroy the main window, the application exits, and the event loop finishes.

Sometimes, you need to create additional windows. For example, you may want to create a custom dialog or a wizard form.

To do that, you can use top-level windows which are instances of the `Toplevel` class.

Unlike the main window, you can create as many top-level windows as you want.

To show a `Toplevel` window from the main window, you follow these steps:

First, create an instance of the `Toplevel` class and set its parent to the root window:

```python
window = tk.Toplevel(root)
```

The moment you create the `Toplevel` window, it'll display on the screen.

Second, add widgets to the `Toplevel` window like you do with the [frames](https://www.pythontutorial.net/tkinter/tkinter-frame/) and [main window](https://www.pythontutorial.net/tkinter/tkinter-window/).

Third, call the `grab_set()` method of the `Toplevel` window instance to allow it to receive events and prevent users from interacting with the main window:

```python
window.grab_set()
```

A simple Tkinter Toplevel Window example
----------------------------------------

The following program displays a window that has one [button](https://www.pythontutorial.net/tkinter/tkinter-button/):

![](Tkinter-Toplevel-Window.png)

When you click the button, it'll open a `Toplevel` window. The `Toplevel` window also consists of a button.

If you click or press the `Close` button, the `Toplevel` window closes.

```python

import tkinter as tk
from tkinter import ttk


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
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
```

How it works.

First, [define a class](https://www.pythontutorial.net/python-oop/python-class/) `Window` that [inherits](https://www.pythontutorial.net/python-oop/python-inheritance/) from the `Toplevel` window. The `Window` will be closed once the `Close` button is clicked.

Second, assign the [command](https://www.pythontutorial.net/tkinter/tkinter-command/) of the **Open a window** button to the `open_window()` method in the `App` class

Third, in the `open_window()` method, create a new instance of the `Window` and call the `grab_set()` method so that it can receive events.

The `grab_set()` method also prevents users from interacting with the main window.

Summary
-------

- Show additional windows by creating instances of the `Toplevel` class.
- Use `grab_set()` method so that the `Toplevel` window can receive events and prevents users from interacting with the main window.

[Previous How to Display a Progress Bar while a Thread is Running in Tkinter](https://www.pythontutorial.net/tkinter/tkinter-thread-progressbar/ "How to Display a Progress Bar while a Thread is Running in Tkinter"){.prev-page-anchor}

[Next Tkinter PhotoImage](https://www.pythontutorial.net/tkinter/tkinter-photoimage/ "Tkinter PhotoImage")
