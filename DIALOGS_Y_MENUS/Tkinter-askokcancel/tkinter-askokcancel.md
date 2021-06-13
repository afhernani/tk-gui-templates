# [Tkinter askokcancel]()

Resumen: en este tutorial, aprenderá a usar la función askokcancel() de Tkinter para mostrar un cuadro de diálogo de confirmación.

## Introducción a la función askokcancel() de Tkinter

La función askokcancel() muestra un diálogo de confirmación que tiene dos botones: Aceptar y Cancelar.

```python
answer = askokcancel(title, message, **options)
```

Si hace clic en el botón Aceptar, la función devuelve Verdadero. Sin embargo, si hace clic en el botón Cancelar, la función devuelve Falso.
Ejemplo de Tkinter askokcancel ()

El siguiente programa muestra un botón **Eliminar todo**. Si hace clic en el botón, el programa mostrará un cuadro de diálogo de confirmación que tiene dos botones: Aceptar y Cancelar.

![](Tkinter-askokcancel-example.png)

Si hace clic en el botón Aceptar, el programa mostrará un cuadro de mensaje que indica que todos los datos se han eliminado correctamente:

![](Tkinter-askokcancel-dialog.png)

![](Tkinter-askokcancel-messagebox.png)

el programa:

```python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING

# create the root window
root = tk.Tk()
root.title('Tkinter Ok/Cancel Dialog')
root.geometry('300x150')

# click event handler


def confirm():
    answer = askokcancel(
        title='Confirmation',
        message='Deleting will delete all the data.',
        icon=WARNING)

    if answer:
        showinfo(
            title='Deletion Status',
            message='The data is deleted successfully')


ttk.Button(
    root,
    text='Delete All',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()

```

El siguiente programa hace lo mismo que el programa anterior, pero utiliza el enfoque de programación orientada a objetos:

```python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Ok/Cancel Dialog')
        self.geometry('300x150')

        delete_button = ttk.Button(
            self,
            text='Delete All',
            command=self.confirm)

        delete_button.pack(expand=True)

    def confirm(self):
        answer = askokcancel(
            title='Confirmation',
            message='Deleting will delete all the data.',
            icon=WARNING)

        if answer:
            showinfo(
                title='Deletion Status',
                message='The data is deleted successfully')


if __name__ == "__main__":
    app = App()
    app.mainloop()
```


Resumen

- Utilice la función askokcancel() de Tkinter para mostrar un cuadro de diálogo de confirmación con dos botones Aceptar y Cancelar.

- La función askokcancel() devuelve Verdadero si hace clic en el botón Aceptar y Falso si hace clic en el botón Cancelar.

