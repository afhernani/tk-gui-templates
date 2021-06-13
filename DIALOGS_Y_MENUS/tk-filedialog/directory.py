from tkinter import filedialog
from tkinter import *

root = Tk()
root.directory =  filedialog.askdirectory()
print (root.directory)
