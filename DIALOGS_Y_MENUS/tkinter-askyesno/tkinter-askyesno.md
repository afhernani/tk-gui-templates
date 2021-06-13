# [Tkinter askyesno](https://www.pythontutorial.net/tkinter/tkinter-askyesno/)

Resumen: en este tutorial, aprenderá a usar la función askyesno() de Tkinter para mostrar un cuadro de diálogo que solicita la confirmación del usuario.

## Introducción a la función askyesno() de Tkinter

A veces, es necesario solicitar la confirmación del usuario. Por ejemplo, si los usuarios hacen clic en el botón Salir, querrá preguntarles si realmente quieren cerrar la aplicación. O simplemente lo hacen accidentalmente:

![](Tkinter-askyesno-dialog.png)

Para mostrar un cuadro de diálogo que solicita la confirmación del usuario, utilice la función askyesno().

El diálogo tendrá un título, un mensaje y dos botones (sí y no).

Cuando hace clic en el botón yes, la función devuelve True. Sin embargo, si hace clic en el botón no, devuelve False.

A continuación se muestra la sintaxis de la función askyesno():

```python
answer = askyesno(title, message, **options)
```

Tenga en cuenta que la respuesta es un valor booleano, verdadero o falso.

Tkinter también tiene otra función llamada askquestion(), que es similar a la función askyesno() excepto que devuelve una cadena con un valor de 'sí' o 'no':

```python
answer = askquestion(title, message, **options)
```

## Ejemplo de función Tkinter askyesno()

El siguiente programa ilustra cómo utilizar la función askyesno() de Tkinter:

![](Tkinter-askyesno.png)

Al hacer clic en el botón 'Quit', se mostrará un cuadro de diálogo de confirmación:

![](Tkinter-askyesno-dialog.png)

Si hace clic en el botón 'yes', la aplicación se cerrará. De lo contrario, se quedará.

```python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

# create the root window
root = tk.Tk()
root.title('Tkinter Yes/No Dialog')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to quit?')
    if answer:
        root.destroy()


ttk.Button(
    root,
    text='Ask Yes/No',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()
```

El siguiente es el mismo programa pero usa el enfoque de programación orientada a objetos:

```python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Yes/No Dialog')
        self.geometry('300x150')

        # Quit button
        quit_button = ttk.Button(self, text='Quit', command=self.confirm)
        quit_button.pack(expand=True)

    def confirm(self):
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to quit?')
        if answer:
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
```


Resumen

- Utilice la función askyesno() de Tkinter para mostrar un cuadro de diálogo que solicita la confirmación del usuario.

- La función askyesno() devuelve True si hace clic en el botón 'yes'; de lo contrario, devuelve False.

- La función askquestion() devuelve una cadena con un valor de 'yes' o 'no' en su lugar.

