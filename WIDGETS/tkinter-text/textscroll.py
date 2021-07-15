import tkinter as tk
import tkinter.scrolledtext as St

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.pack(side="top", fill="both", expand=True)
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.hbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.hbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.hbar.pack(side="bottom", fill="x")
        self.window_frame = tk.Frame(self.canvas)
        self.window_id = self.canvas.create_window((4,4), window=self.window_frame, anchor="ne")
        self.window_frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        self.text_box_list = []
        for n in range(10):
            tb = St.ScrolledText(self.window_frame)
            tb.pack(side="left", fill='both', expand=True)
            self.text_box_list.append(tb)

        self.canvas.update_idletasks()      # refresh canvas

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        '''Set inner windowed frame to same height as canvas'''
        self.canvas.itemconfig(self.window_id, height=event.height)

if __name__ == "__main__":
    root=tk.Tk()
    root.geometry('1000x500+0+0')
    root.bind("<Escape>", exit)
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()