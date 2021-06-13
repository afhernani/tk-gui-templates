[](javascript:void(0) "Back To Top"){.to-top .top-is-visible
.top-fade-out}

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
Spinbox]{.breadcrumb_last aria-current="page"}
:::

Tkinter Spinbox {#tkinter-spinbox .entry-title}
===============

::: {.entry-content}
**Summary**: in this tutorial, you'll learn how to create Tkinter
Spinbox widgets.

Introduction to the Tkinter Spinbox widget
------------------------------------------

A Spinbox widget allows you to select a value from a set of values. The
values can be a range of numbers.

A Spinbox has an area for showing the current value and a pair of
arrowheads.

When you click the upward-pointing arrowhead, the Spinbox advances the
current value to the next higher value in the sequence. If the current
value reaches the maximum value, you can set it to the minimum value.

On the other hand, if you click the downward-pointing arrowhead, the
Spinbox advances the current value to the next lower value in the
sequence. If the current value reaches the lowest value, you can set it
to the maximum value.

Also, you can enter a value directly into the Spinbox widget as if it
were an [Entry](https://www.pythontutorial.net/tkinter/tkinter-entry/)
widget.

To create a Spinbox widget, you use the `ttk.Spinbox` constructor. Here
is a typical options:

``` {.wp-block-code aria-describedby="shcb-language-1" data-shcb-language-name="CSS" data-shcb-language-slug="css"}
        
            
        
     ttk.Spinbox(container, from_, to, textvariable, wrap)Code language: CSS (css)
```

In this syntax:

-   The `container` is the parent component of the Spinbox widget.
-   The `from_` is the minimum value.
-   The `to` is the maximum value.
-   The `textvariable` specifies a `tk.StringVar` object that holds the
    current value of the Spinbox.
-   The `wrap` is a Boolean value. If `wrap` equals `True`, when the
    current value reaches the maximum value, it's set to the lowest
    value if you click the upward-pointing arrowhead and vice versa. In
    case `wrap` equals `False`, it's set to the maximum value if you
    click the downward-pointing arrowhead.

Note that the `ttk.Spinbox` has been available since Python 3.7. If you
use the lower version, you need to use the `tk.Spinbox`.

### Getting the current value

To get the current value of the Spinbox, you can access the
textvariable. For example:

``` {.wp-block-code aria-describedby="shcb-language-2" data-shcb-language-name="PHP" data-shcb-language-slug="php"}
        
            
        
     current_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    container,
    from_=0,
    to=30,
    textvariable=current_value,
    wrap=True)Code language: PHP (php)
```

In this example, the `current_value` holds the current value of the
Spinbox. And you can get it by calling the get method:

``` {.wp-block-code aria-describedby="shcb-language-3" data-shcb-language-name="CSS" data-shcb-language-slug="css"}
        
            
        
     current_value.get()Code language: CSS (css)
```

Also, you can use the `get()` method of the Spinbox object:

``` {.wp-block-code aria-describedby="shcb-language-4" data-shcb-language-name="CSS" data-shcb-language-slug="css"}
        
            
        
     spin_box.get()Code language: CSS (css)
```

### Executing a function

To execute a function when the value of the Spinbox changes, you can
assign that function to the `command` option. For example:

``` {.wp-block-code aria-describedby="shcb-language-5" data-shcb-language-name="PHP" data-shcb-language-slug="php"}
        
            
        
     def value_changed():
    print(current_value.get())

current_value = tk.StringVar(value=0)

spin_box = ttk.Spinbox(
    container,
    from_=0,
    to=30,
    textvariable=current_value,
    command=value_changed)    Code language: PHP (php)
```

In this example, the `value_changed` function will execute automatically
whenever the value of the Spinbox changes.

### Setting discrete steps

To set a list of discrete steps for a Spinbox, you assign a tuple of
discrete numbers to the `values` option like this:

``` {.wp-block-code}
        
            
        
     ttk.Spinbox(
    ...
    values=tuple
    ...
)    
```

Tkinter Spinbox widget examples
-------------------------------

Let's take some example of creating a Spinbox widget.

### 1) A simple Tkinter Spinbox widget example

The following program illustrates how to use the Spinbox:

``` {.wp-block-code aria-describedby="shcb-language-6" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')

# Spinbox
current_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()Code language: Python (python)
```

Output:

::: {.wp-block-image}
![](https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Spinbox-Demo.png){.wp-image-1398
width="302" height="232" sizes="(max-width: 302px) 100vw, 302px"
srcset="https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Spinbox-Demo.png 302w, https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Spinbox-Demo-300x230.png 300w"}
:::

### 2) Tkinter Spinbox with discrete steps

The following example shows how to create a Spinbox with discrete steps:

``` {.wp-block-code aria-describedby="shcb-language-7" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')


# spinbox
current_value = tk.StringVar()
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=50,
    values=(0, 10, 20, 30, 40, 50),
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()Code language: Python (python)
```

Output:

::: {.wp-block-image}
![](https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Spinbox-Discrete-Steps.png){.wp-image-1397
width="302" height="232" sizes="(max-width: 302px) 100vw, 302px"
srcset="https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Spinbox-Discrete-Steps.png 302w, https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Spinbox-Discrete-Steps-300x230.png 300w"}
:::

Summary
-------

-   Use `ttk.Spinbox(container, **options)` to create a Spinbox.
-   Set `wrap=True` to set the current value to the minimum value when
    it reaches the maximum value and vice versa.

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
Slider](https://www.pythontutorial.net/tkinter/tkinter-slider/ "Tkinter Slider"){.prev-page-anchor}
:::

::: {.page-next}
[Next Tkinter
Sizegrip](https://www.pythontutorial.net/tkinter/tkinter-sizegrip/ "Tkinter Sizegrip"){.next-page-anchor}
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

::: {#CodeBadgeTemplate style="display:none"}
::: {.code-badge}
::: {title="Copy to clipboard"}
:::
:::
:::

::: {#searchwp_live_search_results_60613b0b2a161 .searchwp-live-search-results aria-expanded="false" role="listbox" tabindex="0" style="left: 970px; top: 153px; width: 300px;"}
:::
