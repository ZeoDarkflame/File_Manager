import tkinter as tk
import threading
import time

class MainWin():    #this class manages the Main Window

    def __init__(self):
        self.tk = tk.Tk()
        #set Background White
        self.tk.config(bg='white')
        self.tk.title("File Manager")
        #set Size Constant
        self.tk.geometry('1000x500')
        #set Resizable False
        self.tk.resizable(0,0)
        self.header = tk.Frame(self.tk,borderwidth=1,relief=tk.RAISED,bg='white')
        self.header.pack(side=tk.TOP,fill=tk.BOTH)
        self.dirvar = tk.StringVar()
        self.dirlabel = tk.Label(self.header,textvar=self.dirvar,anchor=tk.W,width=200,bg='white')
        self.dirlabel.pack(side=tk.BOTTOM)
        #self.dirvar.set("Testing Text")
        self.backb = tk.Button(self.header,text="<-",relief=tk.FLAT,bg='white')
        self.backb.pack(side=tk.LEFT,padx=3)
        self.left = tk.Frame(self.tk,borderwidth=1,relief=tk.RAISED,bg='white')
        self.left.pack(side=tk.LEFT,fill=tk.BOTH)
        self.leftlab = tk.Label(self.left,text="Auxillary Text",width=20,bg='white')
        self.leftlab.pack()
        self.texframe = tk.Frame(self.tk,padx = 10,pady = 10,bg='white')
        self.texframe.pack(side=tk.LEFT,fill=tk.BOTH)
        self.lablist = []           #these lists hold the labels and text in labels for dynamically
        self.varlist = []           #filling the main text area

        
    
        
if __name__ == "__main__":          #demo the main window if this file is opened directly
    win = MainWin()
    win.tk.mainloop()
