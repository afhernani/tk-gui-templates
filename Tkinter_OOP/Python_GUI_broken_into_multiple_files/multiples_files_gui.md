
### Introduciton

TkInter GUIs can get extremely long very quick. Fortunately they can be
split into multiple files - especially if you give them a class wrapper.
The important thing is that you pass the relavent parent elements so
more widgets can be inserted into the frame or window.

The below example shows how to take the [previous python GUI
example](https://robotic-controls.com/learn/python-guis/basics-tkinter-gui)
and break it into multiple files using Python modules.

### Files

All of the below files must be in the same folder.

#### Main.py

Wow look how the main program is so short now.

```python
from MyTkWindow import *

myWindow = MyTkWindow()
myWindow.start()
```

#### MyTkWindow.py

The main trunk of the code is handled in the the TkWindow file. It
mainly creates the two panels.

```python
from tkinter import *
from MyLeftPanel import *
from MyRightPanel import *

class MyTkWindow:
    def __init__(self):

        self.root = Tk() #Makes the window
        self.root.wm_title("Window Title") #Makes the title that will appear in the top left
        self.root.config(background = "#FFFFFF")

        self.leftFrame = Frame(self.root, width=200, height = 600)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)

        self.rightFrame = Frame(self.root, width=200, height = 300)
        self.rightFrame.grid(row=0, column=1, padx=10, pady=2)

        self.leftPanel = MyLeftPanel(self.root, self.leftFrame)
        self.rightPanel = MyRightPanel(self.root, self.rightFrame)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI
```

So yeah, there is a lot of self now. It\'s not strictly necessary since
you can actually just create local-scope variables because none of these
are referenced again after they are created. However, it\'s always good
to keep things avaialable that you might need later. 

One really nice thing about the [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
gained by these class wrappers is that swapping things around becomes
much easier. For example, you can swap the left and right panels easily
by just changing to this:

```python
     self.leftPanel = MyLeftPanel(self.root, self.rightFrame)
     self.rightPanel = MyRightPanel(self.root, self.leftFrame)
```

Without the encapsulation from classes, you would have to find
everywhere the rightFrame variable was used and change it for leftFrame.

#### MyLeftPanel.py

This is pretty much just a class-ified version of the previous left
panel.

```python
from tkinter import *

class MyLeftPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        #Left Frame and its contents

        Label(self.frame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)


        self.instruct = Label(self.frame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
        self.instruct.grid(row=1, column=0, padx=10, pady=2)

        try:
            self.imageEx = PhotoImage(file = 'image.gif')
            Label(self.frame, image=self.imageEx).grid(row=2, column=0, padx=10, pady=2)
        except:
            print("Image not found")
```

#### MyRightPanel.py

The right panel class here takes advantage of another interesting Python
feature: the [lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) function. It is used here to pass an argument to a callback function.

This lambda basically is just a wrapper function that injects the color
string into the argument for makeCircle. 

```python
from tkinter import *

class MyRightPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        #Right Frame and its contents

        self.circleCanvas = Canvas(self.frame, width=100, height=100, bg='white')
        self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

        self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

        self.redBtn = Button(self.btnFrame, text="Red", command=lambda:self.makeCircle("red"))
        self.redBtn.grid(row=0, column=0, padx=10, pady=2)

        self.yellowBtn = Button(self.btnFrame, text="Yellow", command=lambda:self.makeCircle("yellow"))
        self.yellowBtn.grid(row=0, column=1, padx=10, pady=2)

        self.greenBtn = Button(self.btnFrame, text="Green", command=lambda:self.makeCircle("green") )
        self.greenBtn.grid(row=0, column=2, padx=10, pady=2)

        self.colorLog = Text(self.frame, width = 30, height = 10, takefocus=0)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)


    def makeCircle(self, color):
        self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
        self.colorLog.insert(0.0, color.capitalize() + "\n")
```

To compare, you can actually write the same thing without a lambda. What
you would have to do is define a new function for each call. Like this:

```python
        ...     
                self.redBtn = Button(self.btnFrame, text="Red", command=self.makeRedCircle)
        self.redBtn.grid(row=0, column=0, padx=10, pady=2)

        self.yellowBtn = Button(self.btnFrame, text="Yellow", command=self.makeYellowCircle)
        self.yellowBtn.grid(row=0, column=1, padx=10, pady=2)

        self.greenBtn = Button(self.btnFrame, text="Green", command=self.makeGreenCircle )
        self.greenBtn.grid(row=0, column=2, padx=10, pady=2)

        def makeRedCircle(self):    # this line is replaced by lambda:
                self.makeCircle("red")

        def makeYellowCircle(self): # this line is replaced by lambda:
                self.makeCircle("yellow")

        def makeGreenCircle(self):  # this line is replaced by lambda:
                self.makeCircle("green")

        ...
```

As you can see, that gets pretty messy pretty quickly. It\'s a great way
to create functions that are only used in one place like here, where we
just need to inject an argument into the call of another function.

The repeated creation of the color buttons is also an ideal candidate
for using a class to simplify code.

#### MyRightPanel.py (Class-ier)

Here, the repeated buttons are broken out into a class, which is
duplicated. The advantage in this example is a little less apparent, but
if you were to go back and want to make the buttons bigger or style them
differently or even add a new one, it\'s a lot easier to maintain and
keep the buttons the same.

The big key here is the callback function. The critical thing to notice
to help visualze what is happening is that the function \"makeCircle\"
is not called with () when the class is created. This means that the
function is being passed, rather than the value returned by the
function. 

```python
from tkinter import *

class ColorButton:
    def __init__(self, frame, color, callback):
        self.frame = frame
        self.color = color   # the button's color is retained and accessible
        self.callback = callback

        self.button = Button(self.frame, text=self.color.capitalize(), 
                                     command= lambda: self.callback(self.color) )

        #using pack eliminates the need to count grid spaces
                self.button.pack(side=LEFT) 

class MyRightPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        #Right Frame and its contents

        self.circleCanvas = Canvas(self.frame, width=100, height=100, bg='white')
        self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

        self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

                # significantly simplified button creation
        self.redBtn = ColorButton(self.btnFrame, "red", self.makeCircle)
        self.yellowBtn = ColorButton(self.btnFrame, "yellow", self.makeCircle)
        self.greenBtn = ColorButton(self.btnFrame, "green", self.makeCircle)

        self.colorLog = Text(self.frame, width = 30, height = 10, takefocus=0)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)

    def makeCircle(self, color):
        self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
        self.colorLog.insert(0.0, color.capitalize() + "\n")
```

