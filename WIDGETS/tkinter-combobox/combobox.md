
Tkinter Combobox
================

**Summary**: in this tutorial, you'll learn how to create Tkinter combobox widgets.

Introduction to the Tkinter Combobox
------------------------------------

A combobox is like a combination of an [Entry](https://www.pythontutorial.net/tkinter/tkinter-entry/) widget and a [Listbox](https://www.pythontutorial.net/tkinter/tkinter-listbox/) widget. A combobox allows you to select one value in a list of values. In addition, it allows you to enter a custom value.

To create a combobox, you'll use the `ttk.Combobox()` constructor:

```python
widget_var = tk.StringVar()
combobox = ttk.combobox(container, textvariable=widget_var)
```

The `container` is the [window](https://www.pythontutorial.net/tkinter/tkinter-window/) or [frame](https://www.pythontutorial.net/tkinter/tkinter-frame/) on which the Combobox widget locates

The `textvariable` argument links a variable to the current value of the combobox. The variable needs to be an instance of the `tk.StringVar()`.

To get current selected value, you can use the `get()` method:

```python
current_value = combobox.get()
```

And to set the current value, you can use the `set()` method:

```python
combobox.set(new_value)
```

Once the combobox is created, you can supply a list of predefined values using the `values` option:

```python
compbobox['values'] = ('value1', 'value2', 'value3')
```

By default, you can enter a new entry in the combobox. If you don't want this, you can set the `state` option to `'readonly'`:

```python
compbobox['state'] = 'readonly'
```

To re-enable editing the combobox, you use the `'normal'` state like this:

```python
compbobox['state'] = 'normal'
```

A combobox will generate a `'<<ComboboxSelected>>'` virtual event that you can [bind](https://www.pythontutorial.net/tkinter/tkinter-event-binding/) to whenever its selected value changes:

```python
combobox.bind('<<ComboboxSelected>>', fn)
```

Python Tkinter combobox example
-------------------------------

The following program illustrates how to create a combobox widget:

```python

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')


def month_changed(event):
    msg = f'You selected {month_cb.get()}!'
    showinfo(title='Result', message=msg)


# month of year
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

label = ttk.Label(text="Please select a month:")
label.pack(fill='x', padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()

month_cb = ttk.Combobox(root, textvariable=selected_month)
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.pack(fill='x', padx=5, pady=5)

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()
```

Output:

![](Tkinter-Combobox.png)

Summary
-------

- Use `ttk.Combobox(root, textvariable)` to create a Combobox.
- Set the `state` property to `readonly` to prevent users from entering custom values.
- Bind a function to the `'<<ComboboxSelected>>'` event so that it's invoked automatically when the selected value changes.

[Previous Tkinter Radio Button](https://www.pythontutorial.net/tkinter/tkinter-radio-button/ "Tkinter Radio Button")

[Next Tkinter Listbox](https://www.pythontutorial.net/tkinter/tkinter-listbox/ "Tkinter Listbox")
