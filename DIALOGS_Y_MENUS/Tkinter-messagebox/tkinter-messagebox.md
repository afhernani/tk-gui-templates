# Cuadro de mensajes de [Tkinter messagebox](https://www.pythontutorial.net/tkinter/tkinter-messagebox/)

Resumen: en este tutorial, aprenderá a mostrar varios cuadros de mensajes utilizando el módulo **tkinter.messagebox**.

## Introducción al módulo tkinter.messagebox

Al desarrollar una aplicación Tkinter, a menudo desea notificar a los usuarios sobre los eventos que ocurrieron.

Por ejemplo, cuando los usuarios hacen clic en el botón **button** Guardar, desea notificarles que el registro se ha guardado correctamente.

Si ocurrió un error, por ejemplo, el servidor de la base de datos no es accesible, puede notificar a los usuarios del error.

Cuando la actualización se haya completado pero el registro ya existe, es posible que desee mostrar una advertencia.

Para cubrir todos estos escenarios, puede utilizar varias funciones del módulo **tkinter.messagebox**:

- showinfo(): notifica que una operación se completó correctamente.

- showerror(): notifica que una operación no se ha completado debido a un error.

- showwarrning(): notifica que una operación se completó pero algo no se comportó como se esperaba.

Todas estas funciones aceptan dos argumentos:

```python
showinfo(title, message)
showerror(title, message)
showwarrning(title, message)
```

- El title, se muestra en la barra de título del cuadro de diálogo.

- El message, se muestra en el cuadro de diálogo.

Para abarcar varias líneas del mensaje, puede agregar el carácter de nueva línea '\ n'.


## Ejemplos de cuadro de mensajes de Tkinter

El siguiente programa consta de tres botones. Al hacer clic en un botón, se mostrará el cuadro de mensaje correspondiente.

![](Tkinter-messagebox-application.png)

![](Tkinter-messagebox-showerror.png)

|[](Tkinter-messagebox-showinfo.png)

![](Tkinter-messagebox-showalert.png)

```python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter MessageBox')
root.resizable(False, False)
root.geometry('300x150')

#
options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text='Show an error message',
    command=lambda: showerror(
        title='Error',
        message='This is an error message.')
).pack(**options)

ttk.Button(
    root,
    text='Show an information message',
    command=lambda: showinfo(
        title='Information',
        message='This is an information message.')
).pack(**options)


ttk.Button(
    root,
    text='Show an warning message',
    command=lambda: showwarning(
        title='Warning',
        message='This is a warning message.')
).pack(**options)


# run the app
root.mainloop()

```
Cómo funciona.

Primero, importe los módulos tkinter, tkinter.ttk y tkinter.messagebox:

```python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
```

En segundo lugar, cree la ventana raíz e inicialice sus propiedades:

```python
# create the root window
root = tk.Tk()
root.title('Tkinter MessageBox')
root.resizable(False, False)
root.geometry('300x150')
```

En tercer lugar, cree tres botones y asigne una expresión lambda a la opción de comando de cada botón. Cada expresión lambda muestra un cuadro de mensaje correspondiente.

```python
ttk.Button(
    root,
    text='Show an error message',
    command=lambda: showerror(
        title='Error',
        message='This is an error message.')
).pack(**options)

ttk.Button(
    root,
    text='Show an information message',
    command=lambda: showinfo(
        title='Information',
        message='This is an information message.')
).pack(**options)


ttk.Button(
    root,
    text='Show an warning message',
    command=lambda: showwarning(
        title='Warning',
        message='This is a warning message.')
).pack(**options)
```

Finalmente, muestre la ventana raíz.

```python
root.mainloop()
```

## Resumen

Utilice las funciones showinfo(), showerror(), showwarrning() del módulo tkinter.messagebox para mostrar una información, un error y un mensaje de advertencia.
