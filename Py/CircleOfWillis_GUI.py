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
        first_number = slices-2
    e.delete(0,END)
    e.insert(0,1+(first_number))

    
    slice_2 = data[:, :, int(e.get())]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=0, column=1,columnspan=7)
    
def button_up_double():
    global myImage   
    global myLabel     
    myLabel.grid_forget()
    
    first_number = int(e.get())
    if first_number>= (slices-4):
        first_number = slices-6
    e.delete(0,END)
    e.insert(0,5+(first_number))

    
    slice_2 = data[:, :, int(e.get())]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=0, column=1,columnspan=7)

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
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=0, column=1,columnspan=7)

def button_down_double():
    global myImage   
    global myLabel     
    myLabel.grid_forget()

    first_number = int(e.get())
    if first_number<= 4:
        first_number = 5
    e.delete(0,END)
    e.insert(0,-5+(first_number))
    slice_2 = data[:, :, int(e.get())]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=0, column=1,columnspan=7)
    
# start the window here    
root = Tk()
root.title("Circle of Willis")
root.iconbitmap('CircleW.ico')

# read the data


from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

img      = nib.load('TPH-001_V1.nii')
data     = img.get_fdata()
dims     = data.shape
slices   = dims[2]


# define the slices and the environment to move up and down
e = Entry(root, width = 10, borderwidth = 5,  fg="blue", bg="white")
e.insert(0, "0")
#e.grid(row = 0, column=6)


#print(data[0:2,0:2,0])


Ax_MIP = np.max(data, axis=2)
Sag_MIP= np.max(data, axis=1)
Cor_MIP= np.max(data, axis=0)

Sag_MIP = np.rot90(Sag_MIP, k=3, axes=(1,0))
Cor_MIP = np.rot90(Cor_MIP, k=3, axes=(1,0))


#print(type(q))
slice_2 = data[:, :, int(e.get())]

#plt.imshow(slice_2)
#myImage = ImageTk.PhotoImage(Image.open("Circle_of_Willis.png"))
myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
myLabel       = Label(image=myImage)

Ax_MIP_image  = ImageTk.PhotoImage(image=Image.fromarray(Ax_MIP).resize((320,320)))
Ax_MIP_Label  = Label(image=Ax_MIP_image)
Sag_MIP_image  = ImageTk.PhotoImage(image=Image.fromarray(Sag_MIP).resize((320,120)))
Sag_MIP_Label  = Label(image=Sag_MIP_image)
Cor_MIP_image  = ImageTk.PhotoImage(image=Image.fromarray(Cor_MIP).resize((320,120)))
Cor_MIP_Label  = Label(image=Cor_MIP_image)

button_up            = Button (root, text = ">",padx=10,pady=10, command=button_up)
button_down          = Button (root, text = "<",padx=10,pady=10, command=button_down)
button_up_double     = Button (root, text = ">>",padx=10,pady=10, command=button_up_double)
button_down_double   = Button (root, text = "<<",padx=10,pady=10, command=button_down_double)


myLabel.grid(row=0, column=1,columnspan=7)
Ax_MIP_Label.grid(row=2, column=1,columnspan=7) 
Sag_MIP_Label.grid(row=2, column=8,columnspan=1) 
Cor_MIP_Label.grid(row=2, column=9,columnspan=1) 

button_down_double.grid(row=1, column=1)
button_down.grid(row=1, column=2)
button_up.grid(row=1, column=6)
button_up_double.grid(row=1, column=7)

e.grid(row = 1, column =4, padx = 10, pady= 10)
minLabel = Label(root, text="0").grid(row = 1, column=3)
maxLabel = Label(root, text=slices-1).grid(row = 1, column=5)



#myImage = ImageTk.PhotoImage(slice_2)
#myLabel.pack()
#button_down.pack()
#button_up.pack()




#button_quit = Button(root, text="Exit Programme", command = root.quit)
#button_quit.pack()
  


root.mainloop()