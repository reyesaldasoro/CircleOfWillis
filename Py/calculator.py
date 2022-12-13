# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:45:27 2022

@author: sbbk034
"""

from tkinter import *

root = Tk()
root.title("Circle of Willis")

e = Entry(root, width = 35, borderwidth = 5,  fg="blue", bg="white")
#e.insert(0, "Name???")
#e.grid(row = 0, column=6)
e.grid(row = 0, columnspan =3, padx = 10, pady= 10)

#crrentSum  = 0

def button_clear():
    e.delete(0,END)
    
def button_add():
    first_number = e.get()
    global currentSum
    global math
    math ="addition"
    currentSum = int(first_number)
    e.delete(0,END)
    #e.insert(0,currentSum)
 
def button_subtract():
    first_number = e.get()
    global currentSum
    global math
    math ="minus"
    currentSum = int(first_number)
    e.delete(0,END)
 
def button_multiply():
    first_number = e.get()
    global currentSum
    global math
    math ="times"
    currentSum = int(first_number)
    e.delete(0,END)
 
def button_divide():
    first_number = e.get()
    global currentSum
    global math
    math ="divide"
    currentSum = int(first_number)
    e.delete(0,END)
 
def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,currentSum  + int(second_number))
    
    if math == "minus":
        e.insert(0,currentSum  - int(second_number))

    if math == "times":
        e.insert(0,currentSum  * int(second_number))

    if math == "divide":
        e.insert(0,int(currentSum  / int(second_number)))


def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    return

    
button_0 = Button (root, text = "0",padx=40,pady=20, command= lambda: button_click(0) )
button_1 = Button (root, text = "1",padx=40,pady=20, command=lambda: button_click(1))
button_2 = Button (root, text = "2",padx=40,pady=20, command=lambda: button_click(2))
button_3 = Button (root, text = "3",padx=40,pady=20, command=lambda: button_click(3))
button_4 = Button (root, text = "4",padx=40,pady=20, command=lambda: button_click(4))
button_5 = Button (root, text = "5",padx=40,pady=20, command=lambda: button_click(5))
button_6 = Button (root, text = "6",padx=40,pady=20, command=lambda: button_click(6))
button_7 = Button (root, text = "7",padx=40,pady=20, command=lambda: button_click(7))
button_8 = Button (root, text = "8",padx=40,pady=20, command=lambda: button_click(8))
button_9 = Button (root, text = "9",padx=40,pady=20, command=lambda: button_click(9))

button_add      = Button (root, text = "+",padx=40,pady=20, command=button_add)
button_subtract = Button (root, text = "-",padx=40,pady=20, command=button_subtract)
button_multiply = Button (root, text = "*",padx=42,pady=20, command=button_multiply)
button_divide   = Button (root, text = "/",padx=40,pady=20, command=button_divide)


button_equal = Button (root, text = "=",padx=40,pady=20, command=button_equal)
button_clear = Button (root, text = "Clear",padx=30,pady=20, command=button_clear)





#place buttons
button_0.grid(row=4, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=6, column=0)
button_divide.grid(row=6, column=1)

button_clear.grid(row=6, column=2)
button_equal.grid(row=5, column=2)











#def myClick():
    #myLabel5 = Label(root, text = "done")
    #myLabel5 = Label(root, text = "hello "+ e.get())
    #myLabel5.grid(row = 2, column=6)

#myLabel1 = Label(root, text="Hello World").grid(row = 0, column=0);
#myLabel2 = Label(root, text="Hello World").grid(row = 1, column=1);
#myLabel3 = Label(root, text="Hello World").grid(row = 2, column=2);
#myLabel4 = Label(root, text="Hello World").grid(row = 3, column=3);

#myButton = Button(root, text="Name?", padx=50, pady=10, command=myClick).grid(row = 3, column=0);

#myLabel1.pack();
#myLabel1.grid(row = 0, column=0);
#myLabel2.grid(row = 1, column=1);
#myLabel3.grid(row = 2, column=2);
#myLabel4.grid(row = 9, column=12);

root.mainloop()