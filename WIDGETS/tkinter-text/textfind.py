from tkinter import * 
root = Tk() 
# at top of root, left to right, put a Label, an Entry, and a Button 
fram = Frame(root) 
Label(fram,text='Text to find:').pack(side=LEFT) 
edit = Entry(fram) 
edit.pack(side=LEFT, fill=BOTH, expand=1) 
edit.focus_set( ) 
butt = Button(fram, text='Find') 
butt.pack(side=RIGHT) 
fram.pack(side=TOP) 

# fill rest of root with a Text and put some text there 
text = Text(root) 
text.insert('1.0', '''
Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura che la diritta via era smarrita 
    ''') 
text.pack(side=BOTTOM) 

# action-function for the Button: highlight all occurrences of string 
def find(): 
    # remove previous uses of tag `found', if any 
    text.tag_remove('found', '1.0', END) 
    # get string to look for (if empty, no searching) 
    s = edit.get() 
    if s: 
        # start from the beginning (and when we come to the end, stop) 
        idx = '1.0' 
        while 1: 
            # find next occurrence, exit loop if no more 
            idx = text.search(s, idx, nocase=1, stopindex=END) 
            if not idx: break 
            # index right after the end of the occurrence 
            lastidx = '%s+%dc' % (idx, len(s)) 
            # tag the whole occurrence (start included, stop excluded) 
            text.tag_add('found', idx, lastidx) 
            # prepare to search for next occurrence 
            idx = lastidx 
        # use a red foreground for all the tagged occurrences 
        text.tag_config('found', foreground='red') 
    # give focus back to the Entry field 
    edit.focus_set() 

# install action-function to execute when user clicks Button 
butt.config(command=find) 

# start the whole show (go event-driven) 
root.mainloop()