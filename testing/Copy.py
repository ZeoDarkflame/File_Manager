import tkinter as tk
import shutil as sh
import os
import subprocess as sub

def Callback( ):
    print(str(src_var) + "  " +str(des_var))
    s2 = sub.run("ls",shell = True)
    s1 = sub.run(["cp" , str(src_var) , str(des_var)])
    print("debug")



win = tk.Tk()

win.title("Copy")
src_var = tk.StringVar()
src_lable = tk.Label(win , text = "enter sourse folder").grid(row = 0 ,column = 0)
src_entery = tk.Entry(win , textvariable = src_var).grid(row = 0 ,column = 1)

des_var = tk.StringVar()
des_lable = tk.Label(win , text = "enter Destination Folder").grid(row = 1 ,column = 0)
des_entery = tk.Entry(win , textvariable = des_var).grid(row = 1 ,column = 1)

Sumbit = tk.Button(text = "Copy" , command = Callback )

Sumbit.grid(row=2,column= 0)
win.mainloop()