from tkinter import *


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root = Tk()
root.geometry('1000x500')
frame1 = Frame(root,width=50,height=100)
frame1.pack(side='left')
canvas = Canvas(frame1,bg='white')
frame2 = Frame(canvas)
scroller = Scrollbar(frame1,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=scroller.set)
scroller.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame2,anchor='nw')
#frame2.bind("<Configure>",myfunction)
for i in range(30):
    Button(frame2,text="button " + str(i)).grid(row=i,columns=1)

root.mainloop()

#picked from https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
'''
from tkinter import *

def data():
    for i in range(50):
       Label(frame,text=i).grid(row=i,column=0)
       Label(frame,text="my text"+str(i)).grid(row=i,column=1)
       Label(frame,text="..........").grid(row=i,column=2)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root=Tk()
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()
root.mainloop()
'''