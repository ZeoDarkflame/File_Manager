import tkinter as tk
import shutil as sh
import os
import subprocess as sub

def Callback( ):
    s1 = sub.run(["cp" , src_var.get() , des_var.get()])
    

win = tk.Tk()
win.title("COPY")


src_var = tk.StringVar()
src_lable = tk.Label(win , text = "Enter sourse folder").grid(row = 0 ,column = 0)
src_entery = tk.Entry(win , textvariable = src_var).grid(row = 0 ,column = 1)

des_var = tk.StringVar()
des_lable = tk.Label(win , text = "Enter Destination Folder").grid(row = 1 ,column = 0)
des_entery = tk.Entry(win , textvariable = des_var).grid(row = 1 ,column = 1)

Sumbit = tk.Button(win ,text = "Copy" , command = Callback )

Sumbit.grid(row=2,column= 0)
win.mainloop()