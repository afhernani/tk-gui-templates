import tkinter as tk

root = tk.Tk()
text = tk.Text(root)
label = tk.Label(root)
label.pack(side="top", fill="x")
text.pack(side="top", fill="both", expand=True)

def handle_click(button):
    for (key, name, index) in text.dump("1.0", "end", window=True):
        if name == str(button):
            label.configure(text="You clicked on the button at {}".format(index))
            break

for word in ("one", "two", "three", "four", "five"):
    text.insert("end", word + "\n")
    button = tk.Button(text, text="click me")
    button.configure(command=lambda button=button: handle_click(button))
    text.window_create("insert-1c", window=button)

tk.mainloop()