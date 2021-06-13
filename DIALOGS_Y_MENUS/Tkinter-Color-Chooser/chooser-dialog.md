
[Tkinter Color Chooser](https://www.pythontutorial.net/tkinter/tkinter-color-chooser/)
=====================

**Summary**: in this tutorial, you'll learn how to display a color chooser dialog using the `askcolor()` function from the `tkinter.colorchooser` module.

Introduction to the Tkinter color chooser dialog
------------------------------------------------

To display a native color chooser dialog, you use the `tkinter.colorchooser` module.

First, import the `askcolor()` function from the `tkinter.colorchooser` module:

```python
from tkinter.colorchooser import askcolorCode language: Python (python)
```

Second, call the `askcolor()` function to display the color chooser dialog:

```python
askcolor(color=None, **options)
```

If you select a color, the `askcolor()` function returns a tuple that contains two values that represent the selected color:

-   The first value is the RGB representation.
-   The second value is a hexadecimal representation.

For example:

```python
((255.99609375, 0.0, 255.99609375), '#ff00ff')
```

If you don't select any color from the color chooser dialog, the `askcolor()` function returns `None`.

Tkinter color chooser example
-----------------------------

The following program illustrates how to use the color chooser dialog.

The background of the root window will change to the selected color.

```python

import tkinter as tk
from tkinter.colorchooser import askcolor


root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])


ttk.Button(
    root,
    text='Select a Color',
    command=change_color).pack(expand=True)


root.mainloop()

```

**Output:**

![](Tkinter-Color-Chooser.png)

How it works.

First, import the tkinter and tkinter.colorchooser modules:

```python

import tkinter as tk
from tkinter.colorchooser import askcolor
```

Second, create the root window:

```python

root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')
```

Third, define a function that will be executed when the `'Select a Color'` Button is clicked:

```python
def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])
```

Fourth, create a button and assign the `change_color()` function to its command option:

```python

ttk.Button(
    root,
    text='Select a Color',
    command=change_color).pack(expand=True)
```

Finally, run the `mainloop()` method of the root window:

```python
root.mainloop()
```

Summary
-------

-   Use the `askcolor()` function from `tkinter.colorchooser` module to display a color chooser dialog.
-   The `askcolor()` function returns a tuple of the selected color or None.
