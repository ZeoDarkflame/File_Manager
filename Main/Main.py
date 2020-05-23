from Gui import MainWin
import subprocess
import tkinter as tk
import os

def thispressed(event):
    for i in win.lablist:
        i.config(bg = 'white', fg = 'black')
    event.widget.config(bg = 'blue',fg="white")

def chngdir(event):
    dir = win.varlist[win.lablist.index(event.widget)].get()
    os.chdir(dir)
    maklist()
    print(os.getcwd())

def backpressed(event):
    os.chdir('..')
    maklist()
    print(os.getcwd())

def maklist():
    P = subprocess.Popen("dir",stdout=subprocess.PIPE,shell=True)
    output,err = P.communicate()
    for widget in win.lablist:
        widget.destroy()
    win.lablist.clear()
    win.varlist.clear()
    l = output.decode('utf-8').splitlines()
    l.pop(0)
    l.pop(0)
    l.pop(0)
    win.dirvar.set(l[0][14:])
    l.pop(0)
    l.pop(0)
    l.pop(-1)
    l.pop(-1)
    for i in l:
        if i[36:37] != '.':
            #print(i)
            vari = tk.StringVar()
            lab = tk.Label(win.texframe,textvar=vari,anchor=tk.W,width=200,bg='white')
            lab.pack(side=tk.TOP)
            lab.bind('<Button-1>',thispressed)
            lab.bind('<Double-Button-1>',chngdir)
            vari.set(i[36:])
            win.lablist.append(lab)
            win.varlist.append(vari)

win = MainWin()
maklist()
win.backb.bind('<Button-1>',backpressed)
win.tk.mainloop()
