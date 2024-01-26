# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:45:27 2022

@author: sbbk034
"""

from tkinter import *
from PIL import ImageTk, Image, ImageEnhance
from segment_CircleOfWillis import segment_CircleOfWillis
from tkinterhtml import HtmlFrame
from tkhtmlview  import HTMLLabel, RenderHTML

import plotly.graph_objects as go
import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

from tkinter.filedialog import askopenfilename

global data 

def slider_slices2(self):
    global myImage   
    global myLabel     
    global vasculature0
    global segImage
    global segLabel
    
    myLabel.grid_forget()
    
    first_number = int(slider_slices.get())
    
    if first_number>= (slices-1):
         first_number = slices-2
    e.delete(0,END)
    e.insert(0,1+(first_number))
    new_number = int(e.get())

    slice_2       = data[:, :, new_number]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=1, column=1,columnspan=7)
    slice_3        = 250*vasculature0[:, :, new_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)

def button_up():
    global myImage   
    global myLabel     
    global vasculature0
    global segImage
    global segLabel
    
    myLabel.grid_forget()
    
    first_number = int(e.get())
    if first_number>= (slices-1):
        first_number = slices-2
    e.delete(0,END)
    e.insert(0,1+(first_number))
    new_number = int(e.get())

    
    slice_2 = data[:, :, new_number]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=1, column=1,columnspan=7)
    
    slice_3        = 250*vasculature0[:, :, new_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)
    
def button_up_double():
    global myImage   
    global myLabel     
    global vasculature0
    global segImage
    global segLabel
    
    myLabel.grid_forget()
    
    first_number = int(e.get())
    if first_number>= (slices-4):
        first_number = slices-6
    e.delete(0,END)
    e.insert(0,5+(first_number))
    new_number = int(e.get())

    
    slice_2 = data[:, :, new_number]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=1, column=1,columnspan=7)
    
    slice_3        = 250*vasculature0[:, :, new_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)


def button_down():
    global myImage   
    global myLabel     
    global vasculature0
    global segImage
    global segLabel
    
    myLabel.grid_forget()

    first_number = int(e.get())
    if first_number<= 1:
        first_number = 1
    e.delete(0,END)
    e.insert(0,-1+(first_number))
    new_number = int(e.get())

    
    slice_2 = data[:, :, new_number]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=1, column=1,columnspan=7)
    
    slice_3        = 250*vasculature0[:, :, new_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)
    
def button_down_double():
    global myImage   
    global myLabel     
    global vasculature0
    global segImage
    global segLabel
    
    myLabel.grid_forget()

    first_number = int(e.get())
    if first_number<= 4:
        first_number = 5
    e.delete(0,END)
    e.insert(0,-5+(first_number))
    new_number = int(e.get())

    
    slice_2 = data[:, :, new_number]
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=1, column=1,columnspan=7)
    
    slice_3        = 250*vasculature0[:, :, new_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)

# read the data
def button_read():
    global data
    global filename
    global myImage   
    global myLabel     
    global Ax_MIP_image
    global Sag_MIP_image
    global Cor_MIP_image
    global Ax_MIP_Label
    global Sag_MIP_Label
    global Cor_MIP_Label    
    global maxLabel
    global vasculature0
    global segImage
    global segLabel
    
    filename  = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    img       = nib.load(filename)
    fileLabel = Label(root, text=filename,bd=1, relief=SUNKEN).grid(row = 0, column=8,columnspan=2);
    data      = img.get_fdata()
    new_number = int(e.get())
    slice_2   = data[:, :, new_number]
    
    new_name = filename[:-3]+'npy'
    segmentation_exists = os.path.exists(new_name)
   
    if (segmentation_exists):
        vasculature0=np.load(new_name)
    else:
        # copy the data to a new variable, that will be updated with the segmentation
        vasculature0=data/250

    
    
    myLabel.grid_forget()

    # replace image with new file
    myImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
    myLabel       = Label(image=myImage)
    myLabel.grid(row=1, column=1,columnspan=7)
    
    # recalculate maximum intensity projections
    Ax_MIP        = np.max(data, axis=2)
    Sag_MIP       = np.max(data, axis=1)
    Cor_MIP       = np.max(data, axis=0)
    # rotate sagittal and coronal
    Sag_MIP       = np.rot90(Sag_MIP, k=3, axes=(1,0))
    Cor_MIP       = np.rot90(Cor_MIP, k=3, axes=(1,0))
    # convert into an image from the array and resize
    
    Ax_MIP_image   = ImageTk.PhotoImage(image=Image.fromarray(Ax_MIP).resize((320,320)))
    Sag_MIP_image  = ImageTk.PhotoImage(image=Image.fromarray(Sag_MIP).resize((320,120)))
    Cor_MIP_image  = ImageTk.PhotoImage(image=Image.fromarray(Cor_MIP).resize((320,120)))
    # pass to the labels
    Ax_MIP_Label   = Label(image=Ax_MIP_image)
    Sag_MIP_Label  = Label(image=Sag_MIP_image)
    Cor_MIP_Label  = Label(image=Cor_MIP_image)
    
    
    Ax_MIP_Label.grid(row=3, column=1,columnspan=7) 
    Sag_MIP_Label.grid(row=3, column=8,columnspan=1) 
    Cor_MIP_Label.grid(row=3, column=9,columnspan=1)     
    
    dims     = data.shape
    slices   = dims[2]
    maxLabel = Label(root, text=slices-1).grid(row = 2, column=5)
    
    slice_3        = 250*vasculature0[:, :, new_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)


def segment_data():
    global data
    global filename
    global vasculature0
    global segImage
    global segLabel
    
    # check that the data has not yet been segmented
    #new_name =filename[:-3]+'html'
    new_name = filename[:-3]+'npy'
    segmentation_exists = os.path.exists(new_name)
    
    if (segmentation_exists):
        vasculature0=np.load(new_name)
    else:
        vasculature0 = segment_CircleOfWillis(data)
        np.save(new_name,vasculature0)
        
        
    first_number = int(e.get())
    slice_3        = 250*vasculature0[:, :, first_number]
    segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
    segLabel       = Label(image=segImage)
    segLabel.grid(row=1, column=8)
        




#   ********* start the window here  ***********  
root = Tk()
root.title("Circle of Willis")
root.iconbitmap('CircleW.ico')

# Read the file, open a window to read the file

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(title="Select the *.nii file",filetypes=(("nifti files","*.nii"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file

if filename:
    print(filename)
else:
    print(" No file Selected")    
    #root.destroy()

# read the nifty file
img      = nib.load(filename)
data     = img.get_fdata()

# check if there is already a segmentation of this file
new_name = filename[:-3]+'npy'
segmentation_exists = os.path.exists(new_name)
   
if (segmentation_exists):
    vasculature0=np.load(new_name)
else:
    # copy the data to a new variable, that will be updated with the segmentation
    vasculature0=data/250

dims     = data.shape
slices   = dims[2]
maxLabel = Label(root, text=slices-1).grid(row = 2, column=5)
# display the current file
fileLabel = Label(root, text=filename,bd=1, relief=SUNKEN).grid(row = 0, column=8,columnspan=2,sticky=W+E);


# button to read a different file
button_read     = Button (root, text = "Read File",padx=10,pady=10, command=button_read)
button_read.grid(row = 0, column=4);
button_segment  = Button (root, text = "Segment Data",padx=10,pady=10, command=segment_data)
button_segment.grid(row = 0, column=5);



# define the slices and the environment to move up and down
e = Entry(root, width = 10, borderwidth = 5,  fg="blue", bg="white")
e.insert(0, "0")





Ax_MIP = np.max(data, axis=2)
Sag_MIP= np.max(data, axis=1)
Cor_MIP= np.max(data, axis=0)

Sag_MIP = np.rot90(Sag_MIP, k=3, axes=(1,0))
Cor_MIP = np.rot90(Cor_MIP, k=3, axes=(1,0))

first_number = int(e.get())
slice_2 = data[:, :, first_number]
slice_3 = 250*vasculature0[:, :, first_number]
  
#*********** Calculate the vasculature here ********
#vasculature0 = segment_CircleOfWillis(data)
#rows,cols,levs = vasculature0.shape
#step=2
#X, Y, Z = np.mgrid[85:485:step,70:490:step, 0:levs:1]
#X2=X.flatten()
#Y2=Y.flatten()
#Z2=Z.flatten()
#values=vasculature0[85:485:step,70:490:step,0:levs].flatten()
#fig = go.Figure(data=go.Isosurface(x=X2,y=Y2,z=Z2,value=values,isomin=0.6,isomax=10, opacity=0.5,showscale=False, caps=dict(x_show=False, y_show=False)))
#write_name  = filename[:-3]+'html'
#fig.write_html(write_name, auto_open=True)

#segImage       = ImageTk.PhotoImage(image=Image.fromarray(slice_2S).resize((320,320)))
#segLabel       = Label(image=segImage)

#plt.imshow(slice_2)
#myImage = ImageTk.PhotoImage(Image.open("Circle_of_Willis.png"))


myImage           = ImageTk.PhotoImage(image=Image.fromarray(slice_2).resize((320,320)))
segImage          = ImageTk.PhotoImage(image=Image.fromarray(slice_3).resize((320,320)))
Ax_MIP_image      = ImageTk.PhotoImage(image=Image.fromarray(Ax_MIP).resize((320,320)))
Sag_MIP_image     = ImageTk.PhotoImage(image=Image.fromarray(Sag_MIP).resize((320,120)))
Cor_MIP_preImage  = Image.fromarray(Cor_MIP).resize((320,120))
Cor_MIP_image     = ImageTk.PhotoImage(image=Cor_MIP_preImage)
#vasc_image        = ImageTk.PhotoImage(image=vasc_pre_image)




myLabel           = Label(image=myImage)
Ax_MIP_Label      = Label(image=Ax_MIP_image)
Sag_MIP_Label     = Label(image=Sag_MIP_image)
#Cor_MIP_image  = ImageTk.PhotoImage(image=Image.fromarray(Cor_MIP).resize((320,120)))
Cor_MIP_Label     = Label(image=Cor_MIP_image)



#filterB = ImageEnhance.Brightness(Cor_MIP_preImage)
#Cor_MIP_preImage.filterB(0.5)


button_up            = Button (root, text = ">",padx=10,pady=10,  command=button_up)
button_down          = Button (root, text = "<",padx=10,pady=10,  command=button_down)
button_up_double     = Button (root, text = ">>",padx=10,pady=10, command=button_up_double)
button_down_double   = Button (root, text = "<<",padx=10,pady=10, command=button_down_double)
slider_slices        = Scale  (root, from_= 0, to= slices-1 ,     command=slider_slices2)

myLabel.grid(row=1, column=1,columnspan=7)
segLabel           = Label(image=segImage)
segLabel.grid(row=1,column=8)

Ax_MIP_Label.grid(row=3, column=1,columnspan=7) 
Sag_MIP_Label.grid(row=3, column=8,columnspan=1) 
Cor_MIP_Label.grid(row=3, column=9,columnspan=1) 

button_down_double.grid(row=2, column=1)
button_down.grid(row=2, column=2)
button_up.grid(row=2, column=6)
button_up_double.grid(row=2, column=7)
slider_slices.grid(row=1, column=0)
e.grid(row = 2, column =4, padx = 10, pady= 10)
minLabel = Label(root, text="0").grid(row = 2, column=3)
maxLabel = Label(root, text=slices-1).grid(row = 2, column=5)


html_name = filename[:-3]+'html'
html_exists = os.path.exists(html_name)
print(html_name)
print(html_exists)

if (html_exists):
    html_label = HTMLLabel(root, RenderHTML(html_name))
    html_label.grid(row=1,column=9)


#html_label.pack(fill="both", expand=True)
#html_label.fit_height()

#frame = HtmlFrame(root, horizontal_scrollbar="auto")
#frame.set_content("<html></html>")
#frame.grid(row=1,column=9)

#myImage = ImageTk.PhotoImage(slice_2)
#myLabel.pack()
#button_down.pack()
#button_up.pack()




#button_quit = Button(root, text="Exit Programme", command = root.quit)
#button_quit.pack()
  


root.mainloop()