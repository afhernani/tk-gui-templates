[](javascript:void(0) "Back To Top"){.to-top}

::: {.site-container}
::: {.wrap}
::: {.title-area}
[Python Tutorial - Master Python Programming For Beginners from
Scratch](https://www.pythontutorial.net/)
:::

::: {.wrap}
-   [[Home](https://www.pythontutorial.net/)]{#menu-item-36}
-   [[Getting
    Started](https://www.pythontutorial.net/getting-started/)]{#menu-item-41}
-   [[Basics](https://www.pythontutorial.net/python-basics/)]{#menu-item-42}
-   [[OOP](https://www.pythontutorial.net/python-oop/)]{#menu-item-464}
-   [[Advanced
    Python](https://www.pythontutorial.net/advanced-python/)]{#menu-item-846}
-   [[Tkinter](https://www.pythontutorial.net/tkinter/)]{#menu-item-1320}
:::
:::

::: {.site-inner}
::: {.wrap}
::: {.content-sidebar-wrap}
::: {.content role="main"}
::: {.breadcrumb}
[Home](https://www.pythontutorial.net/) »
[Tkinter](https://www.pythontutorial.net/tkinter/) » [Tkinter
Progressbar]{.breadcrumb_last aria-current="page"}
:::

Tkinter Progressbar {#tkinter-progressbar .entry-title}
===================

::: {.entry-content}
**Summary**: in this tutorial, you'll learn about the Tkinter
Progressbar widget.

Introduction to the Tkinter Progressbar widget
----------------------------------------------

A Progressbar widget allows you to give feedback to the user about the
progress of a long-running task. To create a Progressbar widget, you use
the `ttk.Progressbar` class:

``` {.wp-block-code aria-describedby="shcb-language-1" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     ttk.Progressbar(container, **options)Code language: Python (python)
```

The following shows the typical parameters to create a Progressbar
widget:

``` {.wp-block-code aria-describedby="shcb-language-2" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     ttk.Progressbar(container, orient, length, mode)Code language: Python (python)
```

In this syntax:

-   The `container` is the parent component of the progressbar.
-   The `orient` can be either `'horizontal'` or `'vertical'`.
-   The `length` represents the width of a horizontal progress bar or
    the height of a vertical progressbar.
-   The `mode` can be either `'determinate'` or `'indeterminate'`.

### The indeterminate mode

In the `indeterminate` mode, the progressbar shows an indicator that
bounces back and forth between the ends of the widget.

Typically, you use the `indeterminate` mode when you don't know how to
accurately measure the time that the long-running task takes to
complete.

### The determinate mode

In the `determinate` mode, the progressbar shows an indicator from the
beginning to the end of the widget.

If you know how to measure the relative progress, you can use the
`determinate` mode.

### The important methods of a progressbar

The Progressbar has the following important methods:

-   `start([interval])` -- start moving the indicator every `interval`
    milliseconds. The `interval` defaults to 50ms.
-   `step([delta])` -- increase the indicator value by delta. The
    `delta` defaults to 1 millisecond.
-   `stop()` -- stop moving the indicator of the progressbar.

Tkinter Progressbar examples
----------------------------

Let's take some examples of creating progressbar widgets.

### 1) Tkinter Progressbar in the `indeterminate` mode example

The following program illustrates how to create a progressbar in the
`indeterminate` mode. If you click the `start` button, the progressbar
starts moving the indicator. When you click the `stop` button, the
progressbar stops moving the progress indicator:

``` {.wp-block-code aria-describedby="shcb-language-3" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# start button
start_button = ttk.Button(
    root,
    text='Start',
    command=pb.start
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    root,
    text='Stop',
    command=pb.stop
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()Code language: Python (python)
```

Output:

::: {.wp-block-image}
![](https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Progressbar-indeterminate-example.png){.wp-image-1478
width="302" height="152" sizes="(max-width: 302px) 100vw, 302px"
srcset="https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Progressbar-indeterminate-example.png 302w, https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Progressbar-indeterminate-example-300x151.png 300w"}
:::

How it works.

First, create a horizontal progressbar whose length is 280 pixels and
mode is `'indeterminate'`:

``` {.wp-block-code aria-describedby="shcb-language-4" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)Code language: Python (python)
```

Second, pass the `Progressbar.start` method to the command of the
`start` button:

``` {.wp-block-code aria-describedby="shcb-language-5" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     start_button = ttk.Button(
    root,
    text='Start',
    command=pb.start
)Code language: Python (python)
```

Third, pass the `Progressbar.stop` method to the command of the `stop`
button:

``` {.wp-block-code aria-describedby="shcb-language-6" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     stop_button = ttk.Button(
    root,
    text='Stop',
    command=pb.stop
)Code language: Python (python)
```

### 2) Tkinter Progressbar in the `determinate` mode example

The following program shows how to use a progressbar in the
`determinate` mode:

``` {.wp-block-code aria-describedby="shcb-language-7" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] &lt; 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# start button
start_button = ttk.Button(
    root,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


root.mainloop()Code language: Python (python)
```

Output:

::: {.wp-block-image}
![](https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Progressbar-determinate-example.png){.wp-image-1479
width="302" height="152" sizes="(max-width: 302px) 100vw, 302px"
srcset="https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Progressbar-determinate-example.png 302w, https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Progressbar-determinate-example-300x151.png 300w"}
:::

How it works.

First, create a progressbar in the `determinate` mode:

``` {.wp-block-code aria-describedby="shcb-language-8" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)Code language: Python (python)
```

Second, bind the `progress()` function to the click event of the
`progress` button. Once the button is clicked, the value of the
Progressbar is increased by 20% and the progress label is updated. Also,
the program shows a message box indicating that the progress is
completed if the value reaches 100:

``` {.wp-block-code aria-describedby="shcb-language-9" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     def progress():
    if pb['value'] &lt; 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')Code language: Python (python)
```

Third, bind the `stop()` function to the click event of the `stop`
button. Also, the stop() function wil updates the progress label.

``` {.wp-block-code aria-describedby="shcb-language-10" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     def stop():
    pb.stop()
    value_label['text'] = update_progress_label()Code language: Python (python)
```

Summary
-------

-   Use the `ttk.Progressbar(container, orient, length, mode)` to create
    a progressbar.
-   Use the `indeterminate` mode when the program cannot accurately know
    the relative progress to display.
-   Use the `determinate` mode if you know how to measure the progress
    accurately.
-   Use the `start()`, `step()`, and `stop()` methods to control the
    current value of the progressbar.

::: {.helpful-block-content .wth-theme-thumbs data-title=""}
-   [Was this tutorial helpful ?]{.wth-title}
-   [Yes](#){.wth-green-btn .icon-thumbsup
    .icon1-thumbs-up4}[No](#){.wth-red-btn .icon-thumbsdown
    .icon1-thumbs-down4}
:::
:::

::: {.page-navigation}
::: {.page-previous}
[Previous Tkinter
LabelFrame](https://www.pythontutorial.net/tkinter/tkinter-labelframe/ "Tkinter LabelFrame"){.prev-page-anchor}
:::

::: {.page-next}
[Next Tkinter
Notebook](https://www.pythontutorial.net/tkinter/tkinter-notebook/ "Tkinter Notebook"){.next-page-anchor}
:::
:::
:::

::: {#search-5 .section .widget .widget_search}
::: {.widget-wrap}
:::
:::

::: {#nav_menu-29 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Fundamentals {#fundamentals .widget-title .widgettitle}

::: {.menu-tkinter-fundamentals-container}
-   [[Tkinter Hello,
    World!](https://www.pythontutorial.net/tkinter/tkinter-hello-world/)]{#menu-item-1355}
-   [[Tkinter
    Window](https://www.pythontutorial.net/tkinter/tkinter-window/)]{#menu-item-1672}
-   [[Tk Themed Widgets
    (ttk)](https://www.pythontutorial.net/tkinter/tkinter-ttk/)]{#menu-item-1467}
-   [[Setting Widget's
    Options](https://www.pythontutorial.net/tkinter/tkinter-options/)]{#menu-item-1466}
-   [[Command
    Binding](https://www.pythontutorial.net/tkinter/tkinter-command/)]{#menu-item-1659}
-   [[Event
    Binding](https://www.pythontutorial.net/tkinter/tkinter-event-binding/)]{#menu-item-1658}
-   [[Label](https://www.pythontutorial.net/tkinter/tkinter-label/)]{#menu-item-1673}
-   [[Button](https://www.pythontutorial.net/tkinter/tkinter-button/)]{#menu-item-1674}
-   [[Entry](https://www.pythontutorial.net/tkinter/tkinter-entry/)]{#menu-item-1677}
:::
:::
:::

::: {#nav_menu-30 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Geometry Managers {#geometry-managers .widget-title .widgettitle}

::: {.menu-tkinter-geometry-managers-container}
-   [[Pack](https://www.pythontutorial.net/tkinter/tkinter-pack/)]{#menu-item-1360}
-   [[Grid](https://www.pythontutorial.net/tkinter/tkinter-grid/)]{#menu-item-1359}
-   [[Place](https://www.pythontutorial.net/tkinter/tkinter-place/)]{#menu-item-1358}
:::
:::
:::

::: {#nav_menu-31 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Widgets {#widgets .widget-title .widgettitle}

::: {.menu-tkinter-widgets-container}
-   [[Frame](https://www.pythontutorial.net/tkinter/tkinter-frame/)]{#menu-item-1468}
-   [[Text](https://www.pythontutorial.net/tkinter/tkinter-text/)]{#menu-item-1368}
-   [[Scrollbar](https://www.pythontutorial.net/tkinter/tkinter-scrollbar/)]{#menu-item-1367}
-   [[ScrolledText](https://www.pythontutorial.net/tkinter/tkinter-scrolledtext/)]{#menu-item-2130}
-   [[Separator](https://www.pythontutorial.net/tkinter/tkinter-separator/)]{#menu-item-1366}
-   [[Checkbox](https://www.pythontutorial.net/tkinter/tkinter-checkbox/)]{#menu-item-1365}
-   [[Radio
    Button](https://www.pythontutorial.net/tkinter/tkinter-radio-button/)]{#menu-item-1364}
-   [[Combobox](https://www.pythontutorial.net/tkinter/tkinter-combobox/)]{#menu-item-1363}
-   [[Listbox](https://www.pythontutorial.net/tkinter/tkinter-listbox/)]{#menu-item-1361}
-   [[Slider](https://www.pythontutorial.net/tkinter/tkinter-slider/)]{#menu-item-1394}
-   [[Spinbox](https://www.pythontutorial.net/tkinter/tkinter-spinbox/)]{#menu-item-1402}
-   [[Sizegrip](https://www.pythontutorial.net/tkinter/tkinter-sizegrip/)]{#menu-item-1802}
-   [[LabelFrame](https://www.pythontutorial.net/tkinter/tkinter-labelframe/)]{#menu-item-1418}
-   [[Progressbar](https://www.pythontutorial.net/tkinter/tkinter-progressbar/)]{#menu-item-1482}
-   [[Notebook](https://www.pythontutorial.net/tkinter/tkinter-notebook/)]{#menu-item-1615}
-   [[Treeview](https://www.pythontutorial.net/tkinter/tkinter-treeview/)]{#menu-item-1614}
:::
:::
:::

::: {#nav_menu-32 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Tkinter OOP {#tkinter-oop .widget-title .widgettitle}

::: {.menu-tkinter-oop-container}
-   [[Creating an Object-Oriented
    Window](https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/)]{#menu-item-1545}
-   [[Creating an Object-Oriented
    Frame](https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/)]{#menu-item-1544}
-   [[Developing Tkinter Object-Oriented
    App](https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/)]{#menu-item-1543}
-   [[Switching Between
    Frames](https://www.pythontutorial.net/tkinter/tkraise/)]{#menu-item-1542}
:::
:::
:::

::: {#nav_menu-33 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Dialogs and Menus {#dialogs-and-menus .widget-title .widgettitle}

::: {.menu-tkinter-dialogs-menus-container}
-   [[Message
    Box](https://www.pythontutorial.net/tkinter/tkinter-messagebox/)]{#menu-item-1605}
-   [[Displaying Yes/No
    Dialog](https://www.pythontutorial.net/tkinter/tkinter-askyesno/)]{#menu-item-1604}
-   [[Displaying OK/Cancel
    Dialog](https://www.pythontutorial.net/tkinter/tkinter-askokcancel/)]{#menu-item-1603}
-   [[Displaying Retry/Cancel
    Dialog](https://www.pythontutorial.net/tkinter/tkinter-askretrycancel/)]{#menu-item-1602}
-   [[Displaying Open File
    Dialog](https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/)]{#menu-item-1601}
-   [[Displaying Color
    Chooser](https://www.pythontutorial.net/tkinter/tkinter-color-chooser/)]{#menu-item-1631}
-   [[Menu](https://www.pythontutorial.net/tkinter/tkinter-menu/)]{#menu-item-1606}
-   [[Menubutton](https://www.pythontutorial.net/tkinter/tkinter-menubutton/)]{#menu-item-1825}
-   [[OptionMenu](https://www.pythontutorial.net/tkinter/tkinter-optionmenu/)]{#menu-item-2154}
:::
:::
:::

::: {#nav_menu-34 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Tkinter Application Examples {#tkinter-application-examples .widget-title .widgettitle}

::: {.menu-tkinter-applications-container}
-   [[Temperature Converter
    Application](https://www.pythontutorial.net/tkinter/tkinter-example/)]{#menu-item-1616}
:::
:::
:::

::: {#nav_menu-39 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Modifying Themes & Styles {#modifying-themes-styles .widget-title .widgettitle}

::: {.menu-tkinter-themes-styles-container}
-   [[Ttk
    Theme](https://www.pythontutorial.net/tkinter/tkinter-theme/)]{#menu-item-2070}
-   [[Ttk
    Styles](https://www.pythontutorial.net/tkinter/ttk-style/)]{#menu-item-2069}
-   [[Ttk
    Elements](https://www.pythontutorial.net/tkinter/ttk-elements/)]{#menu-item-2068}
-   [[Ttk Style
    map()](https://www.pythontutorial.net/tkinter/ttk-style-map/)]{#menu-item-2067}
:::
:::
:::

::: {#nav_menu-36 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Tkinter Asynchronous Programming {#tkinter-asynchronous-programming .widget-title .widgettitle}

::: {.menu-tkinter-async-container}
-   [[Developing Multithreading Tkinter
    Apps](https://www.pythontutorial.net/tkinter/tkinter-thread/)]{#menu-item-1756}
-   [[Scheduling an Action: after()
    Method](https://www.pythontutorial.net/tkinter/tkinter-after/)]{#menu-item-1757}
-   [[Displaying a Progressbar While a Thread is
    Running](https://www.pythontutorial.net/tkinter/tkinter-thread-progressbar/)]{#menu-item-1769}
:::
:::
:::
:::
:::
:::

::: {.footer-widgets}
::: {.wrap}
::: {.widget-area .footer-widgets-1 .footer-widget-area}
::: {#custom_html-3 .section .widget_text .widget .widget_custom_html}
::: {.widget_text .widget-wrap}
#### About pythontutorial.net {#about-pythontutorial.net .widget-title .widgettitle}

::: {.textwidget .custom-html-widget}
Pythontutorial.net helps you master Python programming from scratch
fast.
:::
:::
:::

::: {#nav_menu-2 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Site Links {#site-links .widget-title .widgettitle}

::: {.menu-site-links-container}
-   [[Home](https://www.pythontutorial.net/)]{#menu-item-21}
-   [[Contact](https://www.pythontutorial.net/contact/)]{#menu-item-20}
-   [[About](https://www.pythontutorial.net/about/)]{#menu-item-19}
-   [[Privacy
    Policy](https://www.pythontutorial.net/privacy-policy/)]{#menu-item-22}
:::
:::
:::
:::

::: {.widget-area .footer-widgets-2 .footer-widget-area}
::: {#recently_created_pages-2 .section .widget .Recently_Created_Pages}
::: {.widget-wrap}
#### Recent Python Tutorials {#recent-python-tutorials .widget-title .widgettitle}

-   [Python
    None](https://www.pythontutorial.net/advanced-python/python-none/ "Python None")
-   [Python
    Decimal](https://www.pythontutorial.net/advanced-python/python-decimal/ "Python Decimal")
-   [Python
    Rounding](https://www.pythontutorial.net/advanced-python/python-rounding/ "Python Rounding")
-   [Python Float to
    Int](https://www.pythontutorial.net/advanced-python/python-float-to-int/ "Python Float to Int")
-   [Python
    float](https://www.pythontutorial.net/advanced-python/python-float/ "Python float")
:::
:::
:::

::: {.widget-area .footer-widgets-3 .footer-widget-area}
::: {#nav_menu-38 .section .widget .widget_nav_menu}
::: {.widget-wrap}
#### Python References {#python-references .widget-title .widgettitle}

::: {.menu-python-references-container}
-   [[Python String
    Methods](https://www.pythontutorial.net/python-string-methods/)]{#menu-item-1949}
-   [[Python
    MySQL](https://www.mysqltutorial.org/python-mysql/)]{#menu-item-1950}
-   [[Python
    PostgreSQL](https://www.postgresqltutorial.com/postgresql-python/)]{#menu-item-1951}
-   [[Python
    Oracle](https://www.oracletutorial.com/python-oracle/)]{#menu-item-1952}
-   [[Python
    SQLite](https://www.sqlitetutorial.net/sqlite-python/)]{#menu-item-1953}
:::
:::
:::
:::
:::
:::

::: {.wrap}
Copyright © 2021 · by pythontutorial.net. All rights reserved. [Log
in](https://www.pythontutorial.net/wp-login.php)
:::
:::

::: {#ghostery-tracker-tally .ghostery-bottom .ghostery-right .ghostery-collapsed}
::: {#ghostery-box}
::: {#ghostery-count style="background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%; color: rgb(255, 255, 255);"}
1
:::

::: {#ghostery-pb-icons-container}
[]{#ghostery-breaking-tracker .ghostery-pb-tracker
title="Rastreadores de páginas rotas"
style="background: rgba(0, 0, 0, 0) url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+DQo8c3ZnIHdpZHRoPSIxOHB4IiBoZWlnaHQ9IjE4cHgiIHZpZXdCb3g9IjAgMCAxOCAxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4NCiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDQwICgzMzc2MikgLSBodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2ggLS0+DQogICAgPHRpdGxlPmJyZWFraW5ncGFnZTwvdGl0bGU+DQogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+DQogICAgPGRlZnM+PC9kZWZzPg0KICAgIDxnIGlkPSJQdXJwbGUtQm94IiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4NCiAgICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQxNi4wMDAwMDAsIC00NTMuMDAwMDAwKSIgaWQ9ImJhbSEtYnJlYWtpbmctdGhlLXBhZ2UtY29weS0yIiBmaWxsPSIjRkNCQTMzIj4NCiAgICAgICAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQxNi4wMDAwMDAsIDQ1My4wMDAwMDApIj4NCiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNOSwwLjE5NTY1MjE3NCBDNC4xNDQzNjAyNSwwLjE5NTY1MjE3NCAwLjE5NTY1MjE3NCw0LjE0NDM2MDI1IDAuMTk1NjUyMTc0LDkgQzAuMTk1NjUyMTc0LDEzLjg1NTYzOTggNC4xNDQzNjAyNSwxNy44MDQzNDc4IDksMTcuODA0MzQ3OCBDMTMuODU1NjM5OCwxNy44MDQzNDc4IDE3LjgwNDM0NzgsMTMuODU1NjM5OCAxNy44MDQzNDc4LDkgQzE3LjgwNDM0NzgsNC4xNDQzNjAyNSAxMy44NTU2Mzk4LDAuMTk1NjUyMTc0IDksMC4xOTU2NTIxNzQgWiBNMTEuNDg1NTg5OSwxMy40MTA0NDQxIEwxMS4wNzcwNzk4LDEzLjAyMDY3NjggTDEyLjEwMDQ3MTEsMTIuMjE2OTU3OSBMMTEuMDQ2MjQ1MSwxMi4yMTY5NTc5IEwxMS4yMzQ0NzgxLDEwLjg3MDcwODcgTDkuODAzMTgxNDIsMTEuNzk1NzUxMiBMOS40MDMzMzczNCw5LjM0NTA5MzkyIEw4LjY5NDc0MjY5LDExLjA4NjU1MTkgTDcuMzI1NzIwMDksMTAuMTcwOTgxNSBMNy43NTI1Njk3NywxMS45Mjk1NyBMNi41NTQyNDY3MywxMi4zMTE0Nzc1IEw3Ljg4MjM1Nzg3LDEzLjQxMDQ0NDEgTDExLjQ4NTU4OTksMTMuNDEwNDQ0MSBaIE02LjcxNTY3NTcyLDEzLjQxMDQ0NDEgTDUuMDI4NjMxOTcsMTIuMDA2NzU3NiBMNi44Njg0Mzg3MywxMS40MzE5ODE4IEw2LjE2Mzg3NDc3LDguNDg4NTczMDkgTDguMzQ5MzEyODgsOS45NTk5NzUxMiBMOS43MDQwMjY1NCw2LjYxMjQ5MDE1IEwxMC4zNTAzNDcxLDEwLjU1NjcxODIgTDEyLjE5NDk5MDcsOS4zNzY1MzMyOCBMMTEuODk4OTM2OCwxMS40NzY5MjM5IEwxNC4yNjI5MzQzLDExLjQ3NjkyMzkgTDEyLjIxMjkyNzIsMTMuMDc4OTIwMiBMMTIuNTY3MjI0NSwxMy40MTA0NDQxIEwxNS4zMzEyNjc3LDEzLjQxMDQ0NDEgTDE0LjQ3Mzk0MDcsMTIuNTk4NjYzOSBMMTcuMjA3MzUwNiwxMC40NjY4MzM5IEwxMy4wNjA3ODIxLDEwLjQ2NjgzMzkgTDEzLjQ5NjI5NzcsNy4zNDg2OTUgTDExLjA5OTg1MzIsOC44Nzg5NDUwNSBMMTAuMTIxMjAyNiwyLjg5Mjc3MTMgTDcuODc3NzIyNTgsOC40MjU0OTI4NSBMNC41NzA1NDQ0Nyw2LjIwMzk4MDEgTDUuNjY1NDgwNDEsMTAuNzUwMzkyNyBMMi45NTEwMTQ3MiwxMS41OTgyNDc2IEw1LjEzNjQ1MjgzLDEzLjQxMDQ0NDEgTDYuNzE1Njc1NzIsMTMuNDEwNDQ0MSBaIiBpZD0iYnJlYWtpbmdwYWdlIj48L3BhdGg+DQogICAgICAgICAgICA8L2c+DQogICAgICAgIDwvZz4NCiAgICA8L2c+DQo8L3N2Zz4=") repeat scroll 0% 0%; opacity: 0.5;"}[]{#ghostery-slow-tracker
.ghostery-pb-tracker title="Rastreadores lentos"
style="background: rgba(0, 0, 0, 0) url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+DQo8c3ZnIHdpZHRoPSIxN3B4IiBoZWlnaHQ9IjE3cHgiIHZpZXdCb3g9IjAgMCAxNyAxNyIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4NCiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDQwICgzMzc2MikgLSBodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2ggLS0+DQogICAgPHRpdGxlPnNsb3d0cmFja2VyczwvdGl0bGU+DQogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+DQogICAgPGRlZnM+PC9kZWZzPg0KICAgIDxnIGlkPSJQdXJwbGUtQm94IiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4NCiAgICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTM5NS4wMDAwMDAsIC00NTQuMDAwMDAwKSIgaWQ9InNsb3d0cmFja2VycyIgZmlsbD0iI0ZDQkEzMyI+DQogICAgICAgICAgICA8cGF0aCBkPSJNNDAzLjUsNDU0IEMzOTguODEyMjEsNDU0IDM5NSw0NTcuODEyMjEgMzk1LDQ2Mi41IEMzOTUsNDY3LjE4Nzc5IDM5OC44MTIyMSw0NzEgNDAzLjUsNDcxIEM0MDguMTg3NzksNDcxIDQxMiw0NjcuMTg3NzkgNDEyLDQ2Mi41IEM0MTIsNDU3LjgxMjIxIDQwOC4xODc3OSw0NTQgNDAzLjUsNDU0IFogTTQwOS42MDk1ODQsNDY1LjE3ODY1NCBDNDA5LjUzMDI1OSw0NjUuMTU0MDkgNDA4LjY3NzI4Myw0NjQuNzQ2NDIgNDA3LjU2MTA5MSw0NjQuMzYyNjM3IEM0MDguNDg0Mzc4LDQ2My43NDU2MSA0MDkuMDk0NDE4LDQ2Mi42OTM2NDUgNDA5LjA5NDQxOCw0NjEuNTAxNzMzIEM0MDkuMDk0NDE4LDQ1OS42MDU1ODEgNDA3LjU1MTQwMSw0NTguMDYyMzM4IDQwNS42NTUyNDksNDU4LjA2MjMzOCBDNDAzLjc1OTA5Nyw0NTguMDYyMzM4IDQwMi4yMTU4NTQsNDU5LjYwNTU4MSA0MDIuMjE1ODU0LDQ2MS41MDE3MzMgQzQwMi4yMTU4NTQsNDYyLjA0OTM1IDQwMi4zNDUyMDgsNDYyLjU2Njc2OSA0MDIuNTczMjY5LDQ2My4wMjY0OTcgQzQwMi43ODgwMzQsNDYzLjA2ODYzOCA0MDMuMzQ0NDQsNDYzLjE3NTIzMiA0MDQuMjIzNzgyLDQ2My4zMjM5NjggQzQwNS4yMDQ1MzUsNDYzLjQ5MDI4MSA0MDUuODUyNDM2LDQ2My4zNTY0MTkgNDA2LjM5MTAzOSw0NjIuODc2NjM0IEM0MDYuNzI4MTcyLDQ2Mi41NzY0NTkgNDA2LjkyODA2NCw0NjIuMTYzNjA2IDQwNi45NTM1MjksNDYxLjcxMzc5NCBDNDA2Ljk4MDEyMSw0NjEuMjYzOTgxIDQwNi44Mjk1ODMsNDYwLjgyOTk0NCA0MDYuNTI5NDA4LDQ2MC40OTM3MTIgQzQwNi4wNDY5MTksNDU5Ljk1MjQwNSA0MDUuMjE1MTI3LDQ1OS45MDM5NTMgNDA0LjY3MjY5Myw0NjAuMzg1NTQxIEM0MDQuMjM5NTU3LDQ2MC43NzExMjYgNDA0LjE4NTAyMSw0NjEuNDQ0NDkyIDQwNC41NTIxMjcsNDYxLjg1NzM0NiBDNDA0Ljg0MDEzMyw0NjIuMTgwNTA3IDQwNS4zNjk5NDcsNDYyLjIxNzQ2NiA0MDUuNjg2Nzk5LDQ2MS45MzU3NyBDNDA1LjgwMzk4NCw0NjEuODMxODggNDA1Ljg3MzM5NCw0NjEuNjkyODM1IDQwNS44ODA2MDYsNDYxLjU0NDc3NiBDNDA1Ljg4NjY5LDQ2MS40MjQyMSA0MDUuODUwNjMzLDQ2MS4zMTA2MyA0MDUuNzgwOTk4LDQ2MS4yMzQwMDkgQzQwNS43MTg1NzQsNDYxLjE2NTUgNDA1LjYxOTE5Miw0NjEuMTI3NjQxIDQwNS41MTY4OCw0NjEuMTI4NTQyIEM0MDUuNDI5ODkyLDQ2MS4xMzEwMjEgNDA1LjMxNzIxNCw0NjEuMTY1NSA0MDUuMjQ0MTk4LDQ2MS4yMzc2MTUgQzQwNS4yMjYzOTUsNDYxLjI1NDI5MSA0MDUuMjA0NTM1LDQ2MS4yNjQ4ODMgNDA1LjE3OTc0Niw0NjEuMjY0ODgzIEM0MDUuMTI2MTExLDQ2MS4yNjQ4ODMgNDA1LjA4MzA2OCw0NjEuMjE2NDMxIDQwNS4wODMwNjgsNDYxLjE1NzYxMyBDNDA1LjA4MzA2OCw0NjEuMTIxMzMxIDQwNS4wOTc5NDEsNDYxLjA5NDk2NCA0MDUuMTE2NDIxLDQ2MS4wNjk0OTggQzQwNS4yMjYzOTUsNDYwLjkxODk2IDQwNS4zODE0NCw0NjAuODMxNzQ3IDQwNS41MzUzNTksNDYwLjgxODY3NiBDNDA1Ljc0NDAzOSw0NjAuODAxMDk5IDQwNS45MTMwNTcsNDYwLjg2MDgxOCA0MDYuMDQ2OTE5LDQ2MS4wMDc3NTEgQzQwNi4xNzk4NzksNDYxLjE1NDAwNyA0MDYuMjQ5Mjg5LDQ2MS4zNDg0OSA0MDYuMjM3MTIsNDYxLjU2MzI1NSBDNDA2LjIyMzgyNCw0NjEuODA2MTkgNDA2LjExMjk0OCw0NjIuMDMyNDQ4IDQwNS45MjM2NDksNDYyLjIwMDU2NCBDNDA1LjQ1NzE2LDQ2Mi42MTYxMjIgNDA0LjcwNzE3Myw0NjIuNTY2MDkzIDQwNC4yODU1Myw0NjIuMDkzMjk0IEM0MDMuNzg5NzQ1LDQ2MS41MzU5ODcgNDAzLjg1ODQ3OSw0NjAuNjMyMDgxIDQwNC40MzUxNjcsNDYwLjExNzgxNyBDNDA1LjEyMzQwNyw0NTkuNTA1Mjk3IDQwNi4xODI1ODQsNDU5LjU2NjgyIDQwNi43OTQyMDIsNDYwLjI1NTI4NCBDNDA3LjE1NzAyNiw0NjAuNjYyNzMgNDA3LjM0MDAxNiw0NjEuMTg4MjYyIDQwNy4zMDg0NjYsNDYxLjczMzE3NCBDNDA3LjI3NjY5MSw0NjIuMjc4OTg4IDQwNy4wMzQ2NTgsNDYyLjc3OTA1NSA0MDYuNjI2OTg3LDQ2My4xNDE2NTQgQzQwNi4xNjgzODYsNDYzLjU1MDIyNiA0MDUuNjMyMjYyLDQ2My43NDY1MTIgNDA0Ljk0NjUwMiw0NjMuNzQ2NTEyIEM0MDQuNzA1MzcsNDYzLjc0NjUxMiA0MDQuNDQ0ODU3LDQ2My43MjE3MjIgNDA0LjE2MzE2Miw0NjMuNjc0Mzk3IEM0MDMuMTkyMDk5LDQ2My41MDk2NjIgNDAyLjE1NTAwNyw0NjMuMzI0ODY5IDQwMi4wMTU5NjIsNDYzLjMwNTQ4OCBDNDAxLjMxNzEzMSw0NjMuMjEyMTkxIDQwMC43MzYxNjEsNDYyLjczNzU4OSA0MDAuNzE3NjgyLDQ2Mi4wMzk2NTkgTDQwMC44OTQ1ODcsNDU4Ljk4NzY1MyBDNDAwLjg5NDU4Nyw0NTguNzkxMzY3IDQwMC43MzUyNiw0NTguNjMxMTM4IDQwMC41MzgwNzIsNDU4LjYzMTEzOCBDNDAwLjM0MDg4NSw0NTguNjMxMTM4IDQwMC4xODE1NTgsNDU4Ljc5MDQ2NSA0MDAuMTgxNTU4LDQ1OC45ODc2NTMgQzQwMC4xODE1NTgsNDU4Ljk4NzY1MyA0MDAuMjg1NDQ3LDQ2MC44NDE0MzcgNDAwLjI5NzYxNyw0NjEuMDc1NTgzIEM0MDAuMzIwNjAzLDQ2MS41MjAyMTIgMzk5LjkxMTEzLDQ2MS44NzY3MjYgMzk5LjQ2MDQxNiw0NjEuODc2NzI2IEMzOTguOTk4NDM1LDQ2MS44NzY3MjYgMzk4LjU4NzE1OSw0NjEuNTAwODMxIDM5OC42MjM0NDEsNDYxLjAzOTUyNiBDMzk4LjY0MzQ5OCw0NjAuNzg0MTk3IDM5OC42NjQ2ODIsNDYwLjUyMDA3OSAzOTguNjg1ODY1LDQ2MC4yNzI4NjIgTDM5OC43NTk3ODIsNDU5LjAwOTUxMiBDMzk4Ljc1OTc4Miw0NTguODEzMjI2IDM5OC42MDA0NTUsNDU4LjY1Mjk5OCAzOTguNDAzMjY4LDQ1OC42NTI5OTggQzM5OC4yMDYwOCw0NTguNjUyOTk4IDM5OC4wNDY3NTMsNDU4LjgxMjMyNSAzOTguMDQ2NzUzLDQ1OS4wMDk1MTIgTDM5OC4yMjAyNzgsNDYxLjk5OTk5NyBMMzk4LjIyMDI3OCw0NjIuMDA1MTggQzM5OC4yMjAyNzgsNDY0LjA5NzYxNyAzOTkuNDE3MzczLDQ2NS44MDI4OTIgNDAxLjUxMDcxMiw0NjUuODAxMDg5IEM0MDMuNjIyNTMxLDQ2NS43OTgzODUgNDA5LjYwODY4Myw0NjUuODAxMDg5IDQwOS42MDg2ODMsNDY1LjgwMTA4OSBDNDA5Ljc4MTA4MSw0NjUuODAxMDg5IDQwOS45MjAzNTEsNDY1LjY2MTE0MyA0MDkuOTIwMzUxLDQ2NS40ODk0MjEgQzQwOS45MjAzNTEsNDY1LjMxNzAyMyA0MDkuNzczMTkzLDQ2NS4yMzA3MTEgNDA5LjYwOTU4NCw0NjUuMTc4NjU0IFoiPjwvcGF0aD4NCiAgICAgICAgPC9nPg0KICAgIDwvZz4NCjwvc3ZnPg==") repeat scroll 0% 0%; opacity: 0.5;"}[]{#ghostery-non-secure-tracker
.ghostery-pb-tracker title="Rastreadores no seguros"
style="background: rgba(0, 0, 0, 0) url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+DQo8c3ZnIHdpZHRoPSIxOHB4IiBoZWlnaHQ9IjE4cHgiIHZpZXdCb3g9IjAgMCAxOCAxOCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4NCiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDQwICgzMzc2MikgLSBodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2ggLS0+DQogICAgPHRpdGxlPndhcm5pbmc8L3RpdGxlPg0KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPg0KICAgIDxkZWZzPjwvZGVmcz4NCiAgICA8ZyBpZD0iUHVycGxlLUJveCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+DQogICAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0zNzMuMDAwMDAwLCAtNDUzLjAwMDAwMCkiIGlkPSJ3YXJuaW5nIiBmaWxsPSIjRkVCMDMyIj4NCiAgICAgICAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDM3My4wMDAwMDAsIDQ1My4wMDAwMDApIj4NCiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNOSwwLjYzMDQzNDc4MyBDNC4zODQxNDQ5MywwLjYzMDQzNDc4MyAwLjYzMDQzNDc4Myw0LjM4NDE0NDkzIDAuNjMwNDM0NzgzLDkgQzAuNjMwNDM0NzgzLDEzLjYxNTg1NTEgNC4zODQxNDQ5MywxNy4zNjk1NjUyIDksMTcuMzY5NTY1MiBDMTMuNjE1ODU1MSwxNy4zNjk1NjUyIDE3LjM2OTU2NTIsMTMuNjE1ODU1MSAxNy4zNjk1NjUyLDkgQzE3LjM2OTU2NTIsNC4zODQxNDQ5MyAxMy42MTU4NTUxLDAuNjMwNDM0NzgzIDksMC42MzA0MzQ3ODMgWiBNNC42NDI5MjgxMSwxMS43ODk4NTUxIEM1LjI1MDQxMTY1LDExLjc4OTg1NTEgNS43NTY5NTIzNCwxMS4zNjA3NTY3IDUuODc4NzE2OTMsMTAuODgxMzY5NSBDNi4wMDA0ODE1MiwxMS4zNjEyNDM3IDYuNTA3MDIyMjIsMTEuNzIzNzM2OSA3LjExNDM4NCwxMS43MjM3MzY5IEM3LjcyNDE4MTA2LDExLjcyMzczNjkgOC4yMzI2Njk5OSwxMS4zNjUwMTg0IDguMzUxNTEyMjMsMTAuODgyNzA4OSBDOC40NzA5NjMzLDExLjM2NTAxODQgOC45Nzk0NTIyMywxMS43MzY1MjIyIDkuNTg4NzYyMjQsMTEuNzM2NTIyMiBDMTAuMTk0NjYyOCwxMS43MzY1MjIyIDEwLjcwMTIwMzUsMTEuMzk0OTcyNSAxMC44MjM0NTUyLDEwLjkxNjU1OTQgQzEwLjk0NTcwNjgsMTEuMzk0OTcyNSAxMS40NTIyNDc1LDExLjc4OTM2OCAxMi4wNTgyNjk5LDExLjc4OTM2OCBDMTIuMzUzNjcwOCwxMS43ODkzNjggMTIuNjI0NzE4OCwxMS42OTkzODQgMTIuODM5NzU1LDExLjU1OTU5ODIgQzExLjAwOTUxMTUsOC43MTgwOTk3NSAxMi4xNDUzMzE2LDQuMTM3NjgxMTYgMTIuMTQ1MzMxNiw0LjEzNzY4MTE2IEM2Ljk0NjQ3MDYzLDUuMjMxNjE0MjQgNC42NjU4MTk4NSwxMC4xMDAzNzE0IDQuMDU3OTcxMDEsMTEuNjY2MTQyMiBDNC4yMzI5NDY3MywxMS43NDMyMTkyIDQuNDMxNzg4MzEsMTEuNzg5ODU1MSA0LjY0MjkyODExLDExLjc4OTg1NTEgWiIgaWQ9Indhcm5pbmd0cmFja2VycyI+PC9wYXRoPg0KICAgICAgICAgICAgPC9nPg0KICAgICAgICA8L2c+DQogICAgPC9nPg0KPC9zdmc+") repeat scroll 0% 0%; opacity: 0.5;"}
:::

::: {#ghostery-title}
Rastreador
:::

::: {#ghostery-minimize}
[]{#ghostery-minimize-icon}
:::

[]{#ghostery-close
style="background: rgba(0, 0, 0, 0) url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+DQo8c3ZnIHdpZHRoPSIxNXB4IiBoZWlnaHQ9IjE1cHgiIHZpZXdCb3g9IjAgMCAxNSAxNSIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4NCiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDMuNy4yICgyODI3NikgLSBodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2ggLS0+DQogICAgPHRpdGxlPmNvbGxhcHNlIGNvcHkgMjwvdGl0bGU+DQogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+DQogICAgPGRlZnM+PC9kZWZzPg0KICAgIDxnIGlkPSJQdXJwbGUtQm94IiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4NCiAgICAgICAgPGcgaWQ9ImNvbGxhcHNlLWNvcHktMiI+DQogICAgICAgICAgICA8Y2lyY2xlIGlkPSJPdmFsLTMxNSIgZmlsbC1vcGFjaXR5PSIwLjI3MDE1Mzk4NiIgZmlsbD0iI0Q4RDhEOCIgY3g9IjcuNSIgY3k9IjcuNSIgcj0iNy41Ij48L2NpcmNsZT4NCiAgICAgICAgICAgIDxwYXRoIGQ9Ik00LjM2LDQuMzYgTDEwLjU3NDU2MzQsMTAuNTc0NTYzNCIgaWQ9IkxpbmUiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLWxpbmVjYXA9InNxdWFyZSI+PC9wYXRoPg0KICAgICAgICAgICAgPHBhdGggZD0iTTQuMzYsNC4zNiBMMTAuNTc0NTYzNCwxMC41NzQ1NjM0IiBpZD0iTGluZS1Db3B5IiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS1saW5lY2FwPSJzcXVhcmUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDcuNjAwMDAwLCA3LjYwMDAwMCkgc2NhbGUoLTEsIDEpIHRyYW5zbGF0ZSgtNy42MDAwMDAsIC03LjYwMDAwMCkgIj48L3BhdGg+DQogICAgICAgIDwvZz4NCiAgICA8L2c+DQo8L3N2Zz4=") repeat scroll 0% 0%;"}
:::

::: {#ghostery-pb-background}
::: {#ghostery-trackerList}
::: {.ghostery-trackerContainer category="essential"}
[]{#ghostery-no-tracker .ghostery-pb-tracker-list}[Google Tag
Manager]{.ghostery-tracker}
:::
:::
:::
:::

::: {#CodeBadgeTemplate style="display:none"}
::: {.code-badge}
::: {title="Copy to clipboard"}
:::
:::
:::

::: {#searchwp_live_search_results_60614af9ca304 .searchwp-live-search-results aria-expanded="false" role="listbox" tabindex="0" style="left: 970px; top: 153px; width: 300px;"}
:::
