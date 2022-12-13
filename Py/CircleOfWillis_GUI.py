# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:45:27 2022

@author: sbbk034
"""

from tkinter import *
from PIL import ImageTk, Image

import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt


global data 
#from nibabel.testing import data_path
#print(data_path)

def button_up():
    global myImage   
    global myLabel     
    myLabel.grid_forget()
    
    first_number = int(e.get())
    if first_number>= (slices-1):
        first_number = slices-1
    e.delete(0,END)
    e.insert(0,1+(first_number))

    
    slice_2 = data[:, :, int(e.get())]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=0, column=1,columnspan=5)

def changeSlice():
    return

def button_down():
    global myImage   
    global myLabel     
    myLabel.grid_forget()

    first_number = int(e.get())
    if first_number<= 1:
        first_number = 1
    e.delete(0,END)
    e.insert(0,-1+(first_number))
    slice_2 = data[:, :, int(e.get())]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=0, column=1,columnspan=5)


root = Tk()
root.title("Circle of Willis")
root.iconbitmap('CircleW.ico')

e = Entry(root, width = 10, borderwidth = 5,  fg="blue", bg="white")
e.insert(0, "0")
#e.grid(row = 0, column=6)



img      = nib.load('TPH-001_V1.nii')
data     = img.get_fdata()
dims     = data.shape
slices   = dims[2]
#print(data[0:2,0:2,0])


slice_2 = data[:, :, int(e.get())]
print(type(slice_2))
#plt.imshow(slice_2)
#myImage = ImageTk.PhotoImage(Image.open("Circle_of_Willis.png"))
myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2))
myLabel       = Label(image=myImage)

button_up     = Button (root, text = ">>",padx=42,pady=20, command=button_up)
button_down   = Button (root, text = "<<",padx=40,pady=20, command=button_down)


myLabel.grid(row=0, column=1,columnspan=5)
button_down.grid(row=1, column=1)
button_up.grid(row=1, column=5)
e.grid(row = 1, column =3, padx = 10, pady= 10)
minLabel = Label(root, text="0").grid(row = 1, column=2)
maxLabel = Label(root, text=slices).grid(row = 1, column=4)
#myImage = ImageTk.PhotoImage(slice_2)
#myLabel.pack()
#button_down.pack()
#button_up.pack()




#button_quit = Button(root, text="Exit Programme", command = root.quit)
#button_quit.pack()
  


root.mainloop()