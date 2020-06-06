import tkinter as tk
import threading
import time
import subprocess as sub

copywindowopened = False
def oncopy(src_var,des_var):
    print(str(src_var.get()) + "  " +str(des_var.get()))
    #s2 = sub.run("ls",shell = True)
    sub.run(["cp" , str(src_var) , str(des_var)])
    #print("debug")

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
        self.left.pack(side=tk.LEFT,fill=tk.BOTH)       #frame on left
        self.copybutton = tk.Button(self.left,text='Copy',relief = tk.FLAT,bg='white',width=20,pady=3,command = self.oncopybuttonpressed)
        self.copybutton.pack(side=tk.TOP,pady=5,padx=5)
        self.texframe = tk.Frame(self.tk,padx = 10,pady = 10,bg='white')    #frame on center
        self.texframe.pack(side=tk.LEFT,fill=tk.BOTH)
        self.lablist = []           #these lists hold the labels and text in labels for dynamically
        self.varlist = []           #filling the main text area
        self.pressed = ''

    def oncopybuttonpressed(self):
        global copywindowopened
        if copywindowopened == False:
            def onclosing(window):
                global copywindowopened
                copywindowopened = False
                window.destroy()

            global copywin
            copywin = tk.Tk()
            copywin.title("COPY")
            copywin.resizable(0,0)
            copywin.geometry('250x110')
            copywindowopened = True

            src_var = tk.StringVar()
            src_lable = tk.Label(copywin , text = "Filename :",anchor=tk.W,width=10)
            src_lable.grid(row = 0 ,column = 0,padx=10,pady=10)
            src_entry = tk.Entry(copywin , textvariable = src_var)
            src_entry.grid(row = 0 ,column = 1)
            src_entry.insert(0,self.pressed)
            src_entry.focus_set()

            des_var = tk.StringVar()
            des_lable = tk.Label(copywin , text = "To :",anchor=tk.W,width=10)
            des_lable.grid(row = 1 ,column = 0)
            des_entry = tk.Entry(copywin , textvariable = des_var)
            des_entry.grid(row = 1 ,column = 1)

            Sumbit = tk.Button(copywin ,text = "Copy" , command = lambda: oncopy(src_var,des_var) )

            Sumbit.grid(row=2,column= 1,pady=10)
            copywin.protocol('WM_DELETE_WINDOW',lambda:onclosing(copywin))
            copywin.mainloop()
        else:
            copywin.lift()


    
        
if __name__ == "__main__":          #demo the main window if this file is opened directly
    win = MainWin()
    win.tk.mainloop()
