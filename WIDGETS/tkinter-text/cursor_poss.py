import tkinter as tk
import tkinter.ttk as ttk

def actualizar_posicion():
    cursor.configure(text='cursor: {}'.format(texto.index("insert")))
    puntero.configure(text='puntero: {}'.format(texto.index('current')))
    final.configure(text='final: {}'.format(texto.index("end")))

def ajuste_de_linea():
    if texto['wrap'] == 'none':
        texto.configure(wrap='word')
    else:
        texto.configure(wrap='none')

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def handle_click(button):
    for (key, name, index) in texto.dump("1.0", "end", window=True):
        if name == str(button):
            print("you clicked on the button at index {}".format(index))
            print("you clicked on the button at name {}".format(name))
            print("you clicked on the button at key {}".format(key))
            break


v_principal = tk.Tk()

texto = tk.Text(v_principal)
texto.pack(fill=tk.Y)

cursor = tk.Label(v_principal, text='cursor: {}'.format(texto.index("insert")))
cursor.pack()
puntero = tk.Label(v_principal, text='puntero: {}'.format(texto.index("current")))
puntero.pack()
final = tk.Label(v_principal, text='final: {}'.format(texto.index("end")))
final.pack()

ttk.Button(v_principal, text='Actualizar posición', command=actualizar_posicion).pack()
ttk.Button(v_principal, text='Ajuste de línea', command=ajuste_de_linea).pack()

# add button
myboton = ttk.Button(texto, text="mi boton")
myboton1 = ttk.Button(texto, text="elemental")
texto.window_create(tk.END, window=myboton)
texto.window_create(tk.END, window=myboton1)

myboton.configure(command=lambda myboton=myboton: handle_click(myboton))
myboton1.configure(command=lambda myboton1=myboton1: handle_click(myboton1))

texto.bind('<Motion>', motion)

v_principal.mainloop()
