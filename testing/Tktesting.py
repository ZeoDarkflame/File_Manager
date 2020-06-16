from tkinter import *

lablist = []
labtex = []
i = 0
auxframe = None
def clearingeverything(event):
    global auxframe
    try:
        auxframe.destroy()
        auxframe = None
    except:
        pass
    print(auxframe)
def onrightclick(event):
    global auxframe
    print(event.x)
    if auxframe == None:
        auxframe = Frame(top,padx=10,pady=10)
        auxframe.place(x=event.x,y=event.y)
        auxbutton = Button(auxframe,text = "auxillary text")
        auxbutton.pack()
    else:
        auxframe.destroy()
        auxframe = None
        onrightclick(event)
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
frame.pack(side=LEFT,fill = BOTH)
canv = Canvas(frame)
frame2 = Frame(canv,bg='red')
frame2.pack()
scroller = Scrollbar(frame,orient="vertical",command=canv.yview)
canv.config(yscrollcommand=scroller.set)
scroller.pack(side = RIGHT,fill = Y)
canv.create_window((0,0),window=frame,anchor='nw')
canv.pack(side=LEFT)
B = Button(frame2,text="Change Text",relief=FLAT,command=chngtex)
B2 = Button(frame2,text="button 2",relief=FLAT)
B3 = Button(frame2,text="Make One",command=makeone)
B4 = Button(frame2,text="button 4")
B4.pack(side=LEFT)
B.pack(side=LEFT)
B2.pack(side=LEFT)
B3.pack(side=LEFT)
for i in range(20):
    Button(frame2,text = "number " + str(i)).pack(side=BOTTOM)
texframe = Frame(frame2)
texframe.pack(side=LEFT,fill=BOTH)
top.bind('<Button-3>',onrightclick)
top.bind('<Button-1>',clearingeverything)
top.mainloop()

'''
from Tkinter import *

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