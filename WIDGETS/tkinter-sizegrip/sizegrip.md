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
Sizegrip]{.breadcrumb_last aria-current="page"}
:::

Tkinter Sizegrip {#tkinter-sizegrip .entry-title}
================

::: {.entry-content}
**Summary**: in this tutorial, you'll learn how to use the Tkinter
`Sizegrip` widget that allows you to resize the entire application
window.

Introduction to the Tkinter Sizegrip widget
-------------------------------------------

The `Sizegrip` widget typically locates in the bottom right corner of
the window. It allows you to resize the enter application window:

![](https://www.pythontutorial.net/wp-content/uploads/2020/12/Tkinter-Sizegrip-Demo.gif){.wp-image-1800
width="431" height="330"}

To create a `Sizegrip` widget, you use the following syntax:

``` {.wp-block-code aria-describedby="shcb-language-1" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     ttk.Sizegrip(parent, **option)Code language: Python (python)
```

To make sure the `Sizegrip` widget works properly, you need to make the
root window resizable.

If you use the grid geometry manager, you need to configure column and
row sizes.

Tkinter Sizegrip widget example
-------------------------------

The following program displays a `Sizegrip` at the bottom right of the
root window:

``` {.wp-block-code aria-describedby="shcb-language-2" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Sizegrip Demo')
root.geometry('300x200')
root.resizable(True, True)

# grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create the sizegrip
sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)


root.mainloop()Code language: Python (python)
```

Output:

![](https://www.pythontutorial.net/wp-content/uploads/2020/12/tkinter-sizegrip.png){.wp-image-1798
width="333" height="239" sizes="(max-width: 333px) 100vw, 333px"
srcset="https://www.pythontutorial.net/wp-content/uploads/2020/12/tkinter-sizegrip.png 333w, https://www.pythontutorial.net/wp-content/uploads/2020/12/tkinter-sizegrip-300x215.png 300w"}

\
How it works.

First, make sure the root window resizable:

``` {.wp-block-code aria-describedby="shcb-language-3" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     root.resizable(True, True)Code language: Python (python)
```

Second, configure the grid layout:

``` {.wp-block-code aria-describedby="shcb-language-4" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)Code language: Python (python)
```

Third, create a `Sizegrip` widget:

``` {.wp-block-code aria-describedby="shcb-language-5" data-shcb-language-name="Python" data-shcb-language-slug="python"}
        
            
        
     sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)Code language: Python (python)
```

Summary
-------

-   Use the Tkinter `Sizegrip` widget to allow users to resize the
    entire window application.

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
Spinbox](https://www.pythontutorial.net/tkinter/tkinter-spinbox/ "Tkinter Spinbox"){.prev-page-anchor}
:::

::: {.page-next}
[Next Tkinter
LabelFrame](https://www.pythontutorial.net/tkinter/tkinter-labelframe/ "Tkinter LabelFrame"){.next-page-anchor}
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

::: {#searchwp_live_search_results_60613eed0972c .searchwp-live-search-results aria-expanded="false" role="listbox" tabindex="0" style="left: 970px; top: 153px; width: 300px;"}
:::
