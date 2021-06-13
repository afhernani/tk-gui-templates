
[Tkinter askretrycancel](https://www.pythontutorial.net/tkinter/tkinter-askretrycancel/)
======================

**Summary**: in this tutorial, you'll learn how to use the Tkinter `askretrycancel()` function to show a Retry/Cancel confirmation dialog.

Introduction to the Tkinter askretrycancel() function
-----------------------------------------------------

Sometimes, the application performs a task but fails to do so because of an error.

For example, you may want to connect to a database server. However, the database server is currently not reachable. It may be offline for a short period of time.

In this case, you can display a confirmation dialog that allow users to reconnect to the database or just keep the application as is.

To display the Retry/Cancel dialog, you can use the `askretrycancel()` function:

```python
     answer = askretrycancel(title, message, **options)Code language: Python (python)
```

The `askretrycancel()` function returns `True` if the `Retry` button is clicked. If the `Cancel` button is clicked, it returns `False`.

Tkinter `askretrycancel()` function example
-------------------------------------------

The following program shows a button that simulates a bad database
connection:


![](Tkinter-askretrycancel-example.png)

If you click the button, it'll show a Retry/Cancel dialog saying that the database server is not reachable. It'll also request you to reconnect to the database server:


![](Tkinter-askretrycancel-dialog.png)

If you click the Retry button, it'll show a dialog indicating that the program is attempting to reconnect to the database server.


![](Tkinter-askretrycancel-messagebox.png)

[Program:](askretrycancel.py)

```python

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter OK/Retry Dialog')
root.geometry('300x150')

# click event handler
def confirm():
    answer = askretrycancel(
        title='Connection Issue',
        message='The database server is unreachable. Do you want to retry?'
    )
    if answer:
        showinfo(
            title='Information',
            message='Attempt to connect to the database again.')


ttk.Button(
    root,
    text='Connect to the Database Server',
    command=confirm).pack(expand=True)


# start the app
root.mainloop()
Code language: Python (python)
```

Summary
-------

-   Use the `askretrycancel()` function to display a Retry/Cancel dialog to confirm users to carry an operation again.
-   The `askretrycancel()` function returns `True` if the Retry button is clicked. If the Cancel button is clicked, it returns `False`.

