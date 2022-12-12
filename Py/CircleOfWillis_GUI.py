# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:45:27 2022

@author: sbbk034
"""

from tkinter import *

root = Tk()

e = Entry(root, width = 35, fg="blue", bg="white")
e.insert(0, "Name???")
e.grid(row = 1, column=6)
e.get()

def myClick():
    #myLabel5 = Label(root, text = "done")
    myLabel5 = Label(root, text = "hello "+ e.get())
    myLabel5.grid(row = 2, column=6)

myLabel1 = Label(root, text="Hello World").grid(row = 0, column=0);
myLabel2 = Label(root, text="Hello World").grid(row = 1, column=1);
myLabel3 = Label(root, text="Hello World").grid(row = 2, column=2);
myLabel4 = Label(root, text="Hello World").grid(row = 3, column=3);

myButton = Button(root, text="Name?", padx=50, pady=10, command=myClick).grid(row = 3, column=0);

#myLabel1.pack();
#myLabel1.grid(row = 0, column=0);
#myLabel2.grid(row = 1, column=1);
#myLabel3.grid(row = 2, column=2);
#myLabel4.grid(row = 9, column=12);

root.mainloop()