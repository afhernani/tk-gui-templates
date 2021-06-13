
Tkinter Hello, World!
=====================

**Summary**: in this tutorial, you'll learn how to develop the `Tkinter` "Hello, World!" program.

Creating a window
-----------------

The following program shows how to display a [window](https://www.pythontutorial.net/tkinter/tkinter-window/) on the screen:

```python
import tkinter as tk

root = tk.Tk()
root.mainloop()
```

If you execute the program, you'll see the following window:

![](tkinter-hello-world-root-window.png)

How it works.

First, import the `tkinter` module as `tk` to the program:

```python
import tkinter as tk
```

Second, create an instance of the `tk.Tk` class that will create the application window:

```python
root = tk.Tk()
```

By convention, the main window in Tkinter is called `root`. But you can use any other name like `main`.

Third, call the `mainloop()` method of the main window object:

```python
root.mainloop()
```

The `mainloop()` keeps the window visible on the screen. If you don't call the `mainloop()` method, the window will display and disappear immediately. It will be so fast that you may not see its appearance.

Also, the `mainloop()` method keeps the window displaying and running until you close it.

Typically, you call the `mainloop()` method as the last statement in a Tkinter program, after you define all the widgets.

Displaying a label
------------------

Now, it's time to place a component on the window. In `Tkinter`, components are called **widgets**.

The following adds a [label](https://www.pythontutorial.net/tkinter/tkinter-label/)widget to the root window:

```python
import tkinter as tk


root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()
```

Note that you'll learn more about the [`Label` widget](https://www.pythontutorial.net/tkinter/tkinter-label/) in the upcoming tutorial.

If you run the program, you'll see the following output:

![](tkinter-hello-world-label.png)

How it works.

To create a widget that belongs to a container, you use the following syntax:

```python
widget = WidgetName(container, **options)
```

In this syntax:

- The `container` is the parent [window](https://www.pythontutorial.net/tkinter/tkinter-window/) or [frame](https://www.pythontutorial.net/tkinter/tkinter-frame/) that you want to place the widget.
- The `options` is one or more [keyword arguments](https://www.pythontutorial.net/python-basics/python-keyword-arguments/) that specify the configurations of the widget.

In the program, the following creates a `Label` widget placed on the `root` window:

```python
message = tk.Label(root, text="Hello, World!")
```

And the following statement positions the `Label` on the main window:

```python
message.pack()
```

Note that you'll learn more about the `pack()` method later. If you don't call the pack() method, the Tkinter still creates the widget.

However, the widget is invisible.

Summary
-------

- Import `tkinter` module to create a Tkinter desktop application.
- Use `Tk` class to create the main window and call the `mainloop()` method to keep the window displays.
- In Tkinter, components are called widgets.

[Previous: Tkinter](https://www.pythontutorial.net/tkinter/ "Tkinter")

[Next: Tkinter Window](https://www.pythontutorial.net/tkinter/tkinter-window/ "Tkinter Window")
