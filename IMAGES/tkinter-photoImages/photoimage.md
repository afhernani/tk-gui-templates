
Tkinter PhotoImage
==================


**Summary**: in this tutorial, you'll learn how to use the Tkinter PhotoImage widget to display an image on another widget.

Introduction to the Tkinter PhotoImage widget
---------------------------------------------

In Tkinter, some widgets can display an image such as `Label` and `Button`. These widgets take an `image` argument that allows them to display an image.

However, you can't just simply pass the path to an image file to the `image` argument. Instead, you need to create a `PhotoImage` object and pass it the `image` argument.

To create a new `PhotoImage` object, you use the following syntax:

```python
photo_image = tk.PhotoImage(file=path_to_image)
```

In this syntax, you pass the path to the image to the `file` argument to create a new `PhotoImage` object.

Alternatively, you pass a `bytes` object that contains image data to the `data` argument.

After creating a `PhotoImage` object, you can use it in other widgets that accept an `image` argument:

```python
label = ttk.Label(root, image=photo_image)
```

It's important to note that you keep the reference to the `PhotoImage` object in scope for as long as the image will be shown. Otherwise, the image won't appear.

The following example attempts to display an image with the path `'./assets/python.png'` on the root window:

```python

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        python_image = tk.PhotoImage(file='./assets/python.png')
        ttk.Label(self, image=python_image).pack()


if __name__ == &quot;__main__&quot;:
    app = App()
    app.mainloop()

```

If you run the program, you'll notice that the window doesn't show the image.

Why?

That's because the `python_image` is destroyed as soon as the `__init__()` is ended. Since the program has no reference to the `PhotoImage` object, the image vanishes even though you've packed it into the layout.

To fix this issue, you need to make sure the `python_image` doesn't go out of scope after the `__init__()` method ends. For example, you can keep it in the instance of the `App` class such as `self.python_image`:

```python

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')
        self.geometry('320x150')

        self.python_image = tk.PhotoImage(file='./assets/python.png')
        ttk.Label(self, image=self.python_image).pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()

```

Tkinter PhotoImage file formats
-------------------------------

Currently, the `PhotoImage` widget supports the GIF, PGM, PPM, and PNG file formats as of Tkinter 8.6.

To support other file formats such as JPG, JPEG, or BMP, you can use an image library such as Pillow to convert them into a format that the `PhotoImage` widget understands.

In fact, the Pillow library has a Tkinter-compatible `PhotoImage` widget located in the `PIL.ImageTk` module.

The following `pip command` installs the `Pillow` library:

```python
pip install Pillow
```

To use the Pillow library, you follow these steps:

First, import the `Image` and `ImageTk` classes:

```python
from PIL import Image, ImageTk
```

Second, open the image file and create a new `PhotoImage` object:

```python
image = Image.open('./assets/python.jpg')
python_image = ImageTk.PhotoImage(image)
```

Third, assign the `ImageTk.PhotoImage` object to the image option:

```python
image_label = ttk.Label(root, image=python_image)
```

The following program illustrates how to use the `PhotoImage` widget from the Pillow library:

```python
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')

        self.image = Image.open('./assets/python.jpg')
        self.python_image = ImageTk.PhotoImage(self.image)

        ttk.Label(self, image=self.python_image).pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
```

Summary
-------

- Use the Tkinter `PhotoImage` widget to display an image for a `Label` or `Button`.
- Tkinter `PhotoImage` only supports the GIF, PGM, PPM, and PNG file formats.
- Use the `PhotoImage` widget from the `PIL.ImageTk` module to support other file formats.

[prev-page: tkinter Toplevel](../..Tkinter-Asynchronous-Programming/tkinter-toplevel/toplevel.md)

[next: Built-in Function](https://www.pythontutorial.net/python-built-in-functions/ "Python Built-in Functions")