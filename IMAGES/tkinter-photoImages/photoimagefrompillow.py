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


if __name__ == "__main__":
    app = App()
    app.mainloop()

"""
As in Sean's answer, I had to uninstall (I'm using Anaconda Python 3.6, BTW) with

`conda uninstall pillow`

I tried it with PIL, but there was no such package. Uninstalling pillow also meant uninstalling packages that depend on it, in my case "anaconda-navigator" and "scikit-image". After I reinstalled Pillow 4.0.0 with

`conda install pillow=4.0.0`

and tested it with

`python -c "from PIL import Image"`

which, if successful, you don't see an error message, I reinstalled the packages that were uninstalled along with Pillow 4.1.0.

```python
conda install anaconda-navigator
conda install scikit-image
```
"""