# Created by Akshay Ravindran

from __future__ import unicode_literals
from PIL import Image
import PIL.ImageOps    
import glob
import tkinter as tk
import os
import youtube_dl
import sys


# get the Absolute Path

def show_entry_fields():
  y=e1.get()
  print(y)
  image_list = []
  
  print("{}/*.bmp".format(y))
  for filename in glob.glob("{}/*.bmp".format(y)): #assuming bmp
    image=Image.open(filename)
    inverted_image = PIL.ImageOps.invert(image) #Inverts image
    x = str(filename)
    print(x)
    inverted_image.save("{}.png".format(x)) #stores it as bmp
    image_list.append(image)

#User interface
master = tk.Tk()
master.title('Inverter') 
tk.Label(master, text="Folder Absolute Path: ").grid(row=0)
e1 = tk.Entry(master)
e1.insert(10, "Absolute Path")
e1.grid(row=0, column=1)
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='INVERT', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()

tk.mainloop()
