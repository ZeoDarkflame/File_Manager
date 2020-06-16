from Gui import MainWin
import subprocess
import tkinter as tk
import os
optionsframe = None
options = []
emptylabels_to_make = 5
options_not_selected_bg = 'gray88'
options_not_selected_fg = 'black'
options_selected_bg = 'blue'
options_selected_fg = 'white'
inmemory = ''                       #stores the file selected for copy or cut
isdir = False                       #checking whether file or directory
dirinmemory = ''                    #store directory of file to copy or cut
command_selected = ''               #stores type of command to run, copy or cut

def thispressed(event): #change the label to blue when clicked
    for i in win.lablist:
        i.config(bg = 'white', fg = 'black')
    event.widget.config(bg = 'blue',fg="white")
    win.pressed = win.lablist.index(event.widget)
    win.copybutton.config(relief=tk.RAISED)

def optionhover(event):
    for i in options:
        i.config(bg=options_not_selected_bg,fg=options_not_selected_fg)
    event.widget.config(bg=options_selected_bg,fg=options_selected_fg)

def oncopy():
    global dirinmemory,inmemory,command_selected,isdir
    dirinmemory = str(os.getcwd()) +'\\' + win.varlist[win.pressed].get()
    inmemory = win.varlist[win.pressed].get()
    isdir = win.isdir[win.pressed]
    #print(isdir)
    command_selected = 'copy'

def oncut():
    global dirinmemory,inmemory,command_selected,isdir
    dirinmemory = str(os.getcwd()) + '\\' + win.varlist[win.pressed].get()
    inmemory = win.varlist[win.pressed].get()
    isdir = win.isdir[win.pressed]
    #print(inmemory)
    command_selected = 'cut'

def onpaste():
    global command_selected,dirinmemory,inmemory,isdir
    if(command_selected == 'copy'):
        if(isdir):
            os.system('xcopy ' + '"' +  dirinmemory  + '" "' + str(os.getcwd()) + '\\' + inmemory + '"' + ' /e /i /h /c' )
        else:
            os.system('copy ' + '"' + dirinmemory + '" "' + str(os.getcwd()) + '"')
            print('isdir is false')
            print('copy ' + '"' + dirinmemory + '" ".\\' + str(os.getcwd()) + '"')
        maklist()
        command_selected = ''
    if(command_selected == 'cut'):
        #cut
        maklist()
        command_selected = ''
    else:
        maklist()
        pass

def rightclicked(event):
    global optionsframe
    if(event.widget in win.lablist):
        thispressed(event)
        showcopy = True
    else:
        showcopy = False
    if(optionsframe is None):
        optionsframe = tk.Frame(win.texframe)
        try:
            optionsframe.place(x=event.x,y= 21 * win.lablist.index(event.widget) + event.y)
        except:
            optionsframe.place(relx = 0.2,rely= 0.2)
        event.widget.update()
        if(showcopy):
            option1 = tk.Button(optionsframe,text="Copy",relief = tk.FLAT,bg='gray88',command = oncopy)
            option1.pack(side = tk.TOP,fill=tk.X)
            options.append(option1)
            option1.bind('<Motion>',optionhover)
            option2 = tk.Button(optionsframe,text="Cut",relief = tk.FLAT,bg='gray88',command = oncut)
            option2.pack(side = tk.TOP,fill=tk.X)
            options.append(option2)
            option2.bind('<Motion>',optionhover)
        option3 = tk.Button(optionsframe,text="Paste",relief = tk.FLAT,bg='gray88',command = onpaste)
        option3.pack(side = tk.TOP,fill=tk.X)
        options.append(option3)
        option3.bind('<Motion>',optionhover)
    else:
        optionsframe.destroy()
        options.clear()
        optionsframe = None
        rightclicked(event)

def clearprompts(event):
    global optionsframe
    if('button' in str(event.widget)):
        pass
    else:
        try:
            optionsframe.destroy()
            options.clear()
            optionsframe = None
        except:
            pass

def chngdir(event): #change the directory when clicking on a folder
    dir = win.varlist[win.lablist.index(event.widget)].get()
    try:
        os.chdir(dir)
    except:
        pass
    maklist()   #repopulate the main text area with folder and file names of the current folder
    print(os.getcwd())  #print the current directory in the terminal

def backpressed(event): #move to directory(one level up) when pressed back
    os.chdir('..')
    maklist()
    print(os.getcwd())  #print the current directory in the terminal

def maklist():  #to fill the main text area with folder and filenames of the current directory
    P = subprocess.Popen("dir",stdout=subprocess.PIPE,shell=True)   #gets the items in the current directory
    output,_ = P.communicate()        #store the value of the itmes in the output variable
    for widget in win.lablist:
        widget.destroy()            #destroy previously displayed labels to add new ones
    for widget in win.emptylabs:
        widget.destroy()
    win.emptylabs.clear()
    win.lablist.clear()             #clear the lists holding the labels and their texts
    win.varlist.clear()
    l = output.decode('utf-8').splitlines() #convert stored output to readable stings
    l.pop(0)                                #remove empty lines from the output
    l.pop(0)
    l.pop(0)
    #win.dirvar.set(l[0][14:])               #get the current directory from the output
    win.dirvar.set(os.getcwd())             #get current working directroy using separate os command
    l.pop(0)                                #remove some more empty/useless strings
    l.pop(0)
    l.pop(-1)                               #remove data mentioned at the end of output
    l.pop(-1)
    for i in l:                             #store the items names and labels in the lablist and varlist lists to reference later
        if i[36:37] != '.':
            #print(i)
            vari = tk.StringVar()
            lab = tk.Label(win.texframe,textvar=vari,anchor=tk.W,width=200,bg='white')#make a label for each item in the directory
            lab.pack(side=tk.TOP)
            lab.bind('<Button-1>',thispressed)
            lab.bind('<Button-3>',rightclicked)
            lab.bind('<Double-Button-1>',chngdir)
            vari.set(i[36:])                                                          #set the value of variable according to output data
            if 'DIR' in i[:36]:
                win.isdir.append(True)
            else:
                win.isdir.append(False)
            win.lablist.append(lab)
            win.varlist.append(vari)
    for i in range(emptylabels_to_make):
        emptylab = tk.Label(win.texframe,text="",bg='white',width = 200)
        emptylab.pack()
        win.emptylabs.append(emptylab)


win = MainWin()         #make a window from GUI file
maklist()
win.backb.bind('<Button-1>',backpressed)
win.tk.bind('<Button-1>',clearprompts)
print(win.isdir)
win.tk.bind('<Button-3>',rightclicked)
win.tk.mainloop()
