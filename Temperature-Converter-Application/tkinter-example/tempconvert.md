
Tkinter Example
===============

**Summary**: in this tutorial, you'll learn how to build a Tkinter temperature converter application.

Introduction to the Temperature Converter application
-----------------------------------------------------

The following shows the Temperature Converter application that you're going to build. The application converts a temperature from Fahrenheit to Celsius:

![](Tkinter-Example.png)

Basically, the application has a [label](https://www.pythontutorial.net/tkinter/tkinter-label/), an [entry](https://www.pythontutorial.net/tkinter/tkinter-entry/), and a [button](https://www.pythontutorial.net/tkinter/tkinter-button/). When you enter a temperature in Fahrenheit and click the `Convert` button, it'll convert the value in the textbox from Fahrenheit to Celsius.

If you enter a value that cannot be converted to a number, the program will show an error.

To build this application, you follow these steps.

First, import the `tkinter` module, `ttk` submodule, and the `showerror` function from `tkinter.messagebox`:

```python

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
```

Second, create the root window and set its configurations:

```python
# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x70')
root.resizable(False, False)

```

Third, define a function that converts a temperature from Fahrenheit to Celsius:

```python

def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5/9

```

Fourth, create a [frame](https://www.pythontutorial.net/tkinter/tkinter-frame/) that holds form fields:

```python
frame = ttk.Frame(root)
```

Fifth, define an option that will be used by all the form fields:

```python
options = {'padx': 5, 'pady': 5}
```

Sixth, define the label, entry, and button. The label will show the result once you click the `Convert` button:

```python

# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# temperature entry
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# convert button
convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)
```

Finally, place the frame on the root window and run the `mainloop()` method:

```python

frame.grid(padx=10, pady=10)
root.mainloop()
```

Put it all [together](togetherjoin.py).

```python

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x70')
root.resizable(False, False)


def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5/9


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# convert button


def convert_button_clicked():
    """  Handle convert button click event 
    """
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()
```

In this tutorial, you've learned how to develop a simple Tkinter application that converts a temperature from Fahrenheit to Celsius.


[Previous Tkinter OptionMenu](https://www.pythontutorial.net/tkinter/tkinter-optionmenu/ "Tkinter OptionMenu")

[Next Tkinter Object-Oriented Window](https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/ "Tkinter Object-Oriented Window")
