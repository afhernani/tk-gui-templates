
3 Ways to Set Options for a Tk Themed Widget
============================================

**Summary**: in this tutorial, you'll learn how to set options for a Tk themed widget using keyword arguments, a dictionary index, and `config()` method.

When working with [themed widgets](https://www.pythontutorial.net/tkinter/tkinter-ttk/), you often need to set their attributes e.g., text and image.

Tkinter allows you to set the options of a widget using one of the following ways:

- At widget creation, using **[keyword arguments](https://www.pythontutorial.net/python-basics/python-keyword-arguments/)**.
- After widget creation, using a **dictionary index**.
- And use the `config()` method with keyword attributes.

1) Using keyword arguments when creating the widget
---------------------------------------------------

The following illustrates how to use the [keyword arguments](https://www.pythontutorial.net/python-basics/python-keyword-arguments/) to set the `text` option for a label:

```python
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
ttk.Label(root, text='Hi, there').pack()

root.mainloop()
```

Output:

![](tkinter-options-keyword-arguments.png)

2) Using a dictionary index after widget creation
-------------------------------------------------

The following program shows the same label. However, it uses a dictionary index to set the `text` option for the Label widget:

```
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

root.mainloop()
```

The following sets the `text` options for the label:

```python
label['text'] = 'Hi, there'
```

3) Using the config() method with keyword attributes
----------------------------------------------------

The following program illustrates how to use the `config()` method to set the `text` option for the label:

```python
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()
```

Summary
-------

There are three ways to set options for a themed Tkinter widget:

- Use keyword arguments at widget creation.
- Use a dictionary index after widget creation.
- Use the `config()` method with keyword attributes.

[Ttk Widgets](https://www.pythontutorial.net/tkinter/tkinter-ttk/ "Ttk Widgets")

[Tkinter Command Binding](https://www.pythontutorial.net/tkinter/tkinter-command/ "Tkinter Command Binding")
