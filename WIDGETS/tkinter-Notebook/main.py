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


def makenote(text='new notebook'):
    f = ttk.Frame(notebook)
    f.pack(fill='both', expand=True)
    notebook.add(f, text=text)


ttk.Button(frame1, text="new notebook", command=makenote).pack()

root.mainloop()