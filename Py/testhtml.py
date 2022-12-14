# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:09:21 2022

@author: sbbk034
"""
from tkinter import *
from tkinterhtml import HtmlFrame
import urllib

root = Tk()
root.title("Circle of Willis")

frame = HtmlFrame(root, horizontal_scrollbar="auto")
 
#frame.set_content("<html></html>")


#frame.set_content(urllib.request.urlopen("vasculature.html").read().decode())

root.mainloop()