from tkinter import tk

class Text(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)

        # Binding Shortcuts
        self.master.bind("<Delete>", self.Delete_func)

    def Delete_func(self, event):
        def set_default_tag(event):
            if event.char:
                self.master.unbind('<Key>', self.Key_funcid)

            self.text.tag_add("i", "1.0", "end")

        self.text.delete('1.0', 'end')
        self.Key_funcid = self.master.bind('<Key>', set_default_tag)