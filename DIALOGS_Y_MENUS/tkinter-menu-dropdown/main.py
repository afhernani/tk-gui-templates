import tkinter as tk
from dropdown import Dropdown

def dropdown_callback():
    print("Value:", dropdown.get(), "| Index:", dropdown.get_index(), "| Values:", dropdown.values)

root = tk.Tk()

dropdown = Dropdown(root, ("Value 1", "Value 2", "Value 3"), dropdown_callback)

dropdown.pack()

root.mainloop()