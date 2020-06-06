import tkinter as tk
import subprocess as sub
import shutil as sh
import os


def Callback( ):
    print(str(src_var.get()) + "  " +str(new_var.get()))
    #s2 = sub.run("ls",shell = True)
    sub.run(["mv" , str(src_var.get()) , str(new_var.get())])

win = tk.Tk()
win.title("Rename")
win.resizable(0,0)
open = True


src_var = tk.StringVar()
src_lable = tk.Label(win , text = "Filename :",width=10)
src_lable.grid(row = 0 ,column = 0)
src_entry = tk.Entry(win , textvariable = src_var)
src_entry.grid(row = 0 ,column = 1)

new_var = tk.StringVar()
new_lable = tk.Label(win , text = "Filename :",width=10)
new_lable.grid(row = 1 ,column = 0)
new_entry = tk.Entry(win , textvariable = new_var)
new_entry.grid(row = 1 ,column = 1)

Sumbit = tk.Button(win ,text = "Rename" , command = Callback )

Sumbit.grid(row=2,column= 1)



win.mainloop()

