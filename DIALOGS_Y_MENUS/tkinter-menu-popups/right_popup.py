# https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
from tkinter import *

root = Tk()
root.title('Right Click Menu')
root.iconbitmap('collage.ico') # pathdir
root.geometry("500x500")

# etiqueta.
label = Label(root, text="", font=("Helvetica", 30))
label.pack(pady=20)

#comandos asociados
def hello():
    label.config(text="Hello World!!")

def goodbye():
    label.config(text="goodbye World!!")

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

#creando un menu
my_menu = Menu(root, tearoff=False) # linea punteada apagada.
my_menu.add_command(label="say hello", command=hello)
my_menu.add_command(label="say Goodbye", command=goodbye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

# asociamos evento del raton a funcion my_popup
root.bind('<Button-3>', my_popup)
root.mainloop()
