
Tkinter LabelFrame {#tkinter-labelframe .entry-title}
==================

**Summary**: in this tutorial, you'll how to use the Tkinter `LabelFrame` widget to group related widgets.

Introduction to the Tkinter LabelFrame
--------------------------------------

Tkinter `LabelFrame` widget is used to group the related widgets.

For example, you can group [Radiobutton](https://www.pythontutorial.net/tkinter/tkinter-radio-button/) widgets in a `LabelFrame` to make them separate from other widgets.

To create a `LabelFrame` widget, you use the `ttk.LabelFrame`:

```python
lf = ttk.LabelFrame(container, **option)
```

In this syntax, you specify the parent component (`container`) of the `LabelFrame` and one or more options.

A notable option is `text` which specifies a label for the `LabelFrame`.

Tkinter LabelFrame widget example
---------------------------------

The following program illustrates how to create a `LabelFrame` widget that groups three radio buttons:

```python
import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('LabelFrame Demo')

# label frame
lf = ttk.LabelFrame(
    root,
    text='Alignment')

lf.grid(column=0, row=0, padx=20, pady=20)

alignment = tk.StringVar()

# left radio button
left_radio = ttk.Radiobutton(
    lf,
    text='Left',
    value='left',
    variable=alignment
)
left_radio.grid(column=0, row=0, ipadx=10, ipady=10)

# center radio button
center_radio = ttk.Radiobutton(
    lf,
    text='Center',
    value='center',
    variable=alignment
)

center_radio.grid(column=1, row=0, ipadx=10, ipady=10)

# right alignment radiobutton
right_radio = ttk.Radiobutton(
    lf,
    text='Right',
    value='right',
    variable=alignment
)
right_radio.grid(column=2, row=0, ipadx=10, ipady=10)

root.mainloop()

```

Output:

![](Tkinter-LabelFrame-Widget.png)

How it works.

First, create a `LabelFrame` widget and use the grid geometry manager to manage its layout:

```python
lf = ttk.LabelFrame(
    root,
    text='Alignment')

lf.grid(column=0, row=0, padx=20, pady=20)
```

Second, create the three radio buttons whose parent component is the `LabelFrame` widget.

Summary
-------

- Use `LabelFrame` widget to group related widgets into one group.
- Use `ttk.LabelFrame(container, **option)` to create a `LabelFrame` widget.

[Previous Tkinter Sizegrip](https://www.pythontutorial.net/tkinter/tkinter-sizegrip/ "Tkinter Sizegrip")

[Next Tkinter Progressbar](https://www.pythontutorial.net/tkinter/tkinter-progressbar/ "Tkinter Progressbar")
