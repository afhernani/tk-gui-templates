# [Notebook Tkinter](https://www.pythontutorial.net/tkinter/tkinter-notebook/)

Resumen: en este tutorial, aprenderá a usar el widget Tkinter Notebook para crear pestañas.

## Introducción al widget Tkinter Notebook

El widget Notebook le permite seleccionar páginas de contenido haciendo clic en las pestañas:

![](Tkinter-Notebook-Example.png)

Al hacer clic en una de estas pestañas, el widget de Notebook mostrará un panel secundario asociado con la pestaña seleccionada. Normalmente, un panel secundario es un widget de marco.

Para crear un widget de Notebook, use la clase ttk.Notebook de la siguiente manera:

```python
notebook = ttk.Notebook(container,**options)
```

En esta sintaxis, el contenedor es el padre del cuaderno. Normalmente, es la ventana raíz.

El portátil tiene algunas opciones útiles. Por ejemplo, usa las opciones de alto y ancho para especificar el alto y el ancho en píxeles asignados al widget.

Además, puede agregar algo de espacio alrededor del exterior del widget utilizando la opción de relleno.

## Métodos de cuaderno

La clase ttk.Notebook le proporciona muchos métodos útiles que le permiten administrar las pestañas de manera efectiva.

A continuación se describen los más utilizados:

## add(child, \**kwargs)

El método add() agrega un widget secundario a una ventana. El argumento \**kwargs es una o más opciones. Estos son los importantes:

- El child es un widget para agregar al cuaderno.

- La opción text especifica la etiqueta que aparece en la pestaña

- La opción image especifica la imagen que se mostrará en la pestaña.

- Si usa las opciones de text e image, debe usar la opción compuesta. La opción compuesta describe la posición de la imagen en relación con el texto. Puede ser tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT, tk.CENTER. Por ejemplo, tk.LEFT colocaría la imagen a la izquierda del texto.

- La opción de underline que toma cero o un entero positivo. Especifica el carácter en una posición del texto en la pestaña que se subrayará.

## hide(tabId)

El método hide() elimina temporalmente la pestaña identificada por tabId del Notebook. Tabs tiene un índice de base cero. Significa que la primera pestaña comienza en cero.

Para mostrar la pestaña, debe volver a llamar al método add (). No hay un método show() correspondiente.

## forget(child)

El forget() elimina permanentemente el child widget especificado del cuaderno.

## Ejemplo de widget Tkinter Notebook

El siguiente programa muestra cómo crear un bloc de notas con dos pestañas:

```python
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')


root.mainloop()
```

Salida:

![](Tkinter-Notebook.png)

Cómo funciona.

Primero, cree un widget de cuaderno cuyo padre sea la ventana raíz:

```python
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)
```

En segundo lugar, cree dos marcos cuyo padre sea el cuaderno:

```python

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
```

En tercer lugar, agregue estos marcos al cuaderno mediante el método add():

```python
notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')
```
## Resumen.

- Utilice la clase ttk.Notebook para crear un widget de cuaderno.

- Utilice el método add() para agregar una pestaña al cuaderno.

- Utilice el método hide() para eliminar temporalmente una pestaña del cuaderno. Para eliminar una pestaña de forma permanente, utilice el método forget().
- 