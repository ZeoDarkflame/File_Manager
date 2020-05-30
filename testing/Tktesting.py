from tkinter import *

lablist = []
labtex = []
i = 0
def thispressed(event):
    for i in lablist:
        i.config(bg = 'white', fg = 'black')
    event.widget.config(bg = 'blue',fg="white")
def makeone():
    vari = StringVar()
    lab = Label(texframe,textvar=vari,anchor=W,width = 20)
    lab.pack(side=TOP)
    lab.bind("<Button-1>",thispressed)
    vari.set("Demo Text")
    lablist.append(lab)
    labtex.append(vari)
def chngtex():
    global i
    labtex[i].set("Text Changed")
    if i < len(lablist):
        i += 1

top = Tk()
top.title("Testing")
top.geometry('500x500')
top.resizable(0,0)
frame = Frame(top)
frame.pack(side=TOP)
B = Button(frame,text="Change Text",relief=FLAT,command=chngtex)
B2 = Button(frame,text="button 2",relief=FLAT)
B3 = Button(frame,text="Make One",command=makeone)
B4 = Button(frame,text="button 4")
B4.pack(side=LEFT)
B.pack(side=LEFT)
B2.pack(side=LEFT)
B3.pack(side=LEFT)
texframe = Frame(top)
texframe.pack(side=LEFT,fill=BOTH)
top.mainloop()