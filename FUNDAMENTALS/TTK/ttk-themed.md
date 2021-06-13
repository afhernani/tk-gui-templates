
Ttk Widgets
===========

**Summary**: in this tutorial, you'll learn about Tk themed widgets by using the `Tkinter.ttk` module.

Introduction to Tk themed widgets
---------------------------------

Tkinter has two generations of widgets:

- The old classic `tk` widgets. Tkinter introduced them in 1991.
- The newer themed `ttk` widgets added in 2007 with Tk 8.5. The newer Tk themed widgets replace many (but not all) classic widgets.

Note that `ttk` stands for Tk themed. Therefore, Tk themed widgets are the same as `ttk` widgets

The `tkinter.ttk` module contains all the new `ttk` widgets. It's a good practice to always use themed widgets whenever they're available.

The following statements import the classic and the new Tk themed widgets:

```python
import tkinter as tk
from tkinter import ttk
```

And the following program illustrates how to create classic and themed labels:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()
```

Output:

![](Tkinter-ttk.png)

They look similar. However, their appearances depend on the platform on which the program runs.

Advantages of using Tk themed widgets
-------------------------------------

By using the Tk themed widgets, you gain the following advantages:

- Separating the widget's behavior and appearance -- the ttk widgets attempt to separate the code that implements the widgets' behaviors from their appearance through the [styling system](https://www.pythontutorial.net/tkinter/ttk-style/).
- Native look & feel -- the ttk widgets have the native look and feel of the platform on which the program runs.
- Simplify the state-specific widget behaviors -- the ttk widgets simplify and generalize the [state-specific widget behavior](https://www.pythontutorial.net/tkinter/ttk-style-map/).

The ttk widgets
---------------

The following `ttk` widgets replace the Tkinkter widgets with the same names:

- [Button](https://www.pythontutorial.net/tkinter/tkinter-button/)
- [Checkbutton](https://www.pythontutorial.net/tkinter/tkinter-checkbox/)
- [Entry](https://www.pythontutorial.net/tkinter/tkinter-entry/)
- [Frame](https://www.pythontutorial.net/tkinter/tkinter-frame/)
- [Label](https://www.pythontutorial.net/tkinter/tkinter-label/)
- [LabelFrame](https://www.pythontutorial.net/tkinter/tkinter-labelframe/)
- [Menubutton](https://www.pythontutorial.net/tkinter/tkinter-menubutton/)
- [PanedWindow](https://www.pythontutorial.net/tkinter/tkinter-panedwindow/)
- [Radiobutton](https://www.pythontutorial.net/tkinter/tkinter-radio-button/)
- [Scale](https://www.pythontutorial.net/tkinter/tkinter-slider/)
- [Scrollbar](https://www.pythontutorial.net/tkinter/tkinter-scrollbar/)
- [Spinbox](https://www.pythontutorial.net/tkinter/tkinter-spinbox/)

And the following widgets are new and specific to `ttk`:

- [Combobox](https://www.pythontutorial.net/tkinter/tkinter-combobox/)
- [Notebook](https://www.pythontutorial.net/tkinter/tkinter-notebook/)
- [Progressbar](https://www.pythontutorial.net/tkinter/tkinter-progressbar/)
- [Separator](https://www.pythontutorial.net/tkinter/tkinter-separator/)
- [Sizegrip](https://www.pythontutorial.net/tkinter/tkinter-sizegrip/)
- [Treeview](https://www.pythontutorial.net/tkinter/tkinter-treeview/)

Summary
-------

- Tkinter has both classic and themed widgets. The Tk themed widgets are also known as `ttk` widgets.
- The `tkinter.ttk` module contains all the `ttk` widgets.
- Do use `ttk` widgets whenever they're available.

[Tkinter Window](https://www.pythontutorial.net/tkinter/tkinter-window/ "Tkinter Window")

[Set Option](https://www.pythontutorial.net/tkinter/tkinter-options/ "3 Ways to Set Options for a Tk Themed Widget")
