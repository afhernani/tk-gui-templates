# [Introducción a Tkinter Notebook](https://www.educba.com/tkinter-notebook/)

![](Tkinter-Notebook.jpg)

En Python, el cuaderno Tkinter se define como pestañas para controlar las pestañas que proporciona la biblioteca ttk y dicho widget con pestañas se usa para permitir navegar de una página a otra, lo que se puede hacer usando la pestaña de índice. En general, este widget de cuaderno se define como un área o pestaña que permite a los usuarios seleccionar páginas de contenido requeridas por el usuario, y esto se hace presionando o haciendo clic en las pestañas que se crean en el área superior del cuaderno principal y después de configurar dicho cuaderno principal, podemos agregar fácilmente las pestañas y cada clic en estas pestañas, el widget del cuaderno mostrará el panel secundario asociado.

# Funcionamiento del cuaderno Tkinter

En este artículo, discutimos el widget de cuaderno de Tkinter en Python. Este widget actúa como pestañas o podemos decir cuaderno con pestañas. Este widget se obtiene de la biblioteca ttk que es útil para administrar un conjunto de ventanas y comenzará a mostrar una ventana cada vez. Por lo tanto, podemos decir que los usuarios pueden seleccionar la ventana esclava relacionada con la pestaña para cambiar la ventana de visualización actual. Este widget de cuaderno utiliza algunos métodos para agregar y eliminar pestañas, como add () para agregar pestañas y algunos otros métodos para ocultar temporalmente las pestañas o eliminar las pestañas. Este widget también proporciona una colección de opciones para cada pestaña que generalmente se utilizan para controlar las apariencias y el comportamiento de las pestañas dentro de los widgets, donde estas opciones se clasifican como opciones estándar, opciones específicas del widget y opciones de pestañas y usos del widget del cuaderno. ID de pestaña para hacer referencia a otra pestaña dentro de los widgets para cambiar de una página a otra.

En la siguiente sección, veamos la sintaxis del cuaderno Tkinter, que se puede declarar como formulario de comando y también como formulario de método.

Sintaxis:

```ttk.notebook(root, **options)```

En la sintaxis anterior, podemos ver que el widget del cuaderno se obtiene del módulo ttk y tiene 2 parámetros: el parámetro raíz que especifica la ventana principal o maestra, y las opciones del segundo parámetro se clasifican en opciones estándar, opciones de pestaña, opciones de widget como clase, cursor, peso, relleno, estado, texto, imagen, etc.

Hay algunos métodos proporcionados por el widget del cuaderno, como add() para agregar pestañas, cget() puede obtener el valor actual de la opción de configuración, hide() para ocultar las pestañas, index() para obtener el índice en el numérico valor de la pestaña especificada, etc.

En Python, Tkinter es un módulo para desarrollar aplicaciones basadas en GUI, mientras que el widget del cuaderno se obtiene del módulo ttk que se considera una extensión del módulo Tkinter o podemos decir la mejora de este módulo Tkinter. Entonces, cuando estamos usando este widget de cuaderno, tenemos que importar el módulo ttk que se usa para crear pestañas en las ventanas y puede mostrar una ventana a la vez y la ventana secundaria está asociada con cada una de las pestañas creadas y estas pestañas generalmente se usan siempre que el usuario quiere mostrar algún mensaje de la viuda.

Let us see a simple example of creating tabs in the window using a notebook widget of ttk module.

# Example

Code:

```python
from Tkinter import *
import Tkinter as tk
import ttk
import tkMessageBox
master = tk.Tk()
master.geometry('500x200')
def func():
tkMessageBox.showinfo( "Hello Educba", "Click on the tabs to view the content")
b1 = Button( master, text='Click me for next step', background = 'Red', fg = '#000000', command = func)
b1.pack()
tc = ttk.Notebook(master)
t1 = ttk.Frame(tc)
t2 = ttk.Frame(tc)
tc.add(t1, text ='Notebook tab1')
tc.add(t2, text ='Notebook tab2')
tc.pack(expand = 1, fill ="both")
ttk.Label(t1,
text ="Hello Educba Technology Institute").grid(column = 3,
row = 3)
ttk.Label(t2,
text ="Notebook widget demonstration").grid(column = 3,
row = 3)
master.mainloop()
```

Output:

![](tkinter-notebook-1-1.png)

![](tkinter-notebook-1-2.png)

En el artículo anterior, podemos ver que primero estamos importando los módulos Tkinter para desarrollar GUI, el módulo ttk para usar el widget del cuaderno para la creación de pestañas dentro de la ventana principal, el módulo tkmessagebox para mostrar cualquier mensaje en el cuadro de diálogo emergente y en En el ejemplo anterior, aparecerá el mensaje cuando hagamos clic en el widget de botón en la ventana. Se mostrará como "haga clic en las pestañas para ver el contenido" para que el usuario pueda cambiar entre las ventanas de una en una utilizando estas pestañas creadas. usando el widget del cuaderno. En este programa, hemos pasado la ventana principal al cuaderno() para que podamos tener control sobre las pestañas para cambiar y mostrar el contenido a medida que se crean las pestañas, necesitamos marcos separados para hacerlo. Por lo tanto, para cada pestaña, hemos utilizado el método frame y hemos pasado los nombres de las pestañas a este método frame(). Luego, usando la función add() estamos agregando el nombre a cada pestaña usando el argumento de texto y hemos nombrado las pestañas como t1 como “Pestaña del cuaderno1”, t2 como “Pestaña del cuaderno2”. Luego, para mostrar el contenido haciendo clic en cada pestaña que tenemos para la pestaña “Pestaña del cuaderno 1”, mostramos el contenido como “Hola Educba Technology Institute” y para la pestaña “Pestaña del cuaderno 2” mostramos “Demostración del widget del cuaderno” y se muestra este contenido usando la función label() donde también toma un argumento de texto para el contenido y donde el contenido debe mostrarse puede ser usado por la función grid() y aquí tenemos que mostrar el mensaje en la columna 3 y la fila 3 para ambas pestañas. Y la salida de todo el programa se puede ver en las capturas de pantalla anteriores.

## Conclusión

En este artículo, concluimos que el módulo Python ttk se utiliza como una extensión o mejora del módulo Tkinter. En el módulo ttk, proporciona algunos widgets nuevos y en este artículo, hemos discutido uno de esos widgets llamado widget de cuaderno que se usa para la creación de pestañas, de modo que al usar el widget de cuaderno podemos alternar entre las ventanas, pero una a la vez y también mostrar el contenido de la ventana. En este artículo, hemos visto la sintaxis del widget del cuaderno y las opciones como cursor, peso, altura, etc. que usa y algunos métodos como add(), Label, etc. En este artículo, también vimos un ejemplo simple que tiene dos pestañas en la misma ventana principal, pero cuando se hace clic en las pestañas, estamos cambiando de una ventana a otra de una en una.

# Recommended Articles

This is a guide to Tkinter Notebook. Here we discuss the Introduction and working of Tkinter Notebook along with an example and code implementation. You may also have a look at the following articles to learn more –

[Tkinter LabelFrame](https://www.educba.com/tkinter-labelframe/)
[Tkinter Combobox](https://www.educba.com/tkinter-combobox/)
[Tkinter after](https://www.educba.com/tkinter-after/)
[Tkinter Colors](https://www.educba.com/tkinter-colors/)


