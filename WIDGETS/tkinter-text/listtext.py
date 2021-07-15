import tkinter as tk
from PIL import Image, ImageTk
import os
import cv2

root = tk.Tk()
myText = tk.Text(root)
myText.pack()

text = """ACAACATACGAGCCGGAAGCATAAAG
TGTAAAGCCTGGGGTGCCTAATGAGT
GAGCTAACTCACATTAGGCTGAATTA
GGCGCGCCT"""

mylist = text.splitlines()
Images = []
frames_in_dir = os.listdir('Images')
path_f = os.path.abspath('Images')
for frame in frames_in_dir:
    frm = os.path.join(path_f, frame)
    load = Image.open(frm)
    render = ImageTk.PhotoImage(load)
    # img = Label(self, image=render)
    # img.image = render
    # img.place(x=0, y=0)
    Images.append(render)

'''
for row in range(len(mylist)):    
    myText.insert('end', mylist[row])
    myText.insert("end", '\n')
    myText.window_create('end', window=tk.Frame(myText, width=180), stretch=1)
    myText.insert("end", '\n')
'''

frames = []  # store the frames
for row in range(len(mylist)):    
    myText.insert('end', mylist[row])
    myText.insert("end", '\n')
    frames.append(tk.Frame(myText, width=180)) # create frame and store it in frames
    myText.window_create('end', window=tk.Label(myText, image=Images[row]), stretch=1)
    myText.insert("end", '\n')

# add a label to each frame
# for i, frame in enumerate(frames, 1):
#    tk.Label(frame, text=f"Hello in frame #{i}").pack()

root.mainloop()
