import tkinter as tk
import shutil as sh
import os
import subprocess as sub

def Callback( ):
    print(str(src_var.get()) + "  " +str(des_var.get()))
    #s2 = sub.run("ls",shell = True)
    sub.run(["cp" , str(src_var) , str(des_var)])
    #print("debug")



win = tk.Tk()
win.title("COPY")
win.resizable(0,0)
open = True


src_var = tk.StringVar()
src_lable = tk.Label(win , text = "Filename :",anchor=tk.W,width=10)
src_lable.grid(row = 0 ,column = 0)
src_entry = tk.Entry(win , textvariable = src_var)
src_entry.grid(row = 0 ,column = 1)
src_entry.focus_set()

des_var = tk.StringVar()
des_lable = tk.Label(win , text = "To :",anchor=tk.W,width=10)
des_lable.grid(row = 1 ,column = 0)
des_entry = tk.Entry(win , textvariable = des_var)
des_entry.grid(row = 1 ,column = 1)

Sumbit = tk.Button(win ,text = "Copy" , command = Callback )

Sumbit.grid(row=2,column= 1)
win.mainloop()