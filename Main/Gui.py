import tkinter as tk
import threading
import time

class MainWin():    #this class manages the Main Window

    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("File Manager")
        self.tk.geometry('1000x500')
        self.tk.resizable(0,0)
        self.header = tk.Frame(self.tk,borderwidth=1,relief=tk.RAISED)
        self.header.pack(side=tk.TOP,fill=tk.BOTH)
        self.backb = tk.Button(self.header,text="<-",relief=tk.FLAT)
        self.backb.pack(side=tk.LEFT,padx=3)
        self.left = tk.Frame(self.tk,borderwidth=1,relief=tk.RAISED)
        self.left.pack(side=tk.LEFT,fill=tk.BOTH)
        self.leftlab = tk.Label(self.left,text="Auxillary Text",width=20)
        self.leftlab.pack()
        self.tk.mainloop()
        
    
        
if __name__ == "__main__":
    win = MainWin()
