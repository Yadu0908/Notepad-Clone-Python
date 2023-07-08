from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

root=Tk()
root.geometry("640x432")
root.title("NoteX")
# root.config(background="Red")
root.iconbitmap("notepad.ico")


def file():
    print("You just clicked the file button")

#we created a fucntion call save as which will save our file.

def saveas():
    file=filedialog.asksaveasfile()
    file_save= file.write(text.get(1.0, END))
    file.close()

def color():
    color=colorchooser.askcolor()
    print(color)
    root.config(background=color[1])
    


menubar= Menu(root, font=("Calibri (Body)",14))         #it will create a menubar

#fILE

m1= Menu(menubar, tearoff=0, font=("Calibri (Body)",10))    #item inside the menubar

m1.add_command(label="New")     #first item of menubar
m1.add_command(label="New file")

m1.add_separator()          #it will create a seprate line b/w menubar items

m1.add_command(label="Open")

m1.add_separator()

m1.add_command(label="Save")

m1.add_command(label="Save as", command=saveas)

m1.add_command(label="Quit", command=quit)

menubar.add_cascade(label="File", menu=m1)


#EDIT

m2= Menu(menubar, tearoff=0)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_separator()
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
m2.add_separator()
m2.add_command(label="Find")
m2.add_command(label="Replace")

menubar.add_cascade(label="Edit", menu=m2)

#THEME


m6= Menu(menubar, tearoff=0)

background=m6.add_command(label="Background", command=color)
foreground=m6.add_command(label="Foreground", command=color)
menubar.add_cascade(label="Theme", menu=m6)


#FORMAT

m3= Menu(menubar, tearoff=0)
m3.add_command(label="Word Wrap")
m3.add_command(label="Font...")
menubar.add_cascade(label="Format", menu=m3)

#STATUS BAR

m4= Menu(menubar, tearoff=0)
m4_1= Menu(m4, tearoff=0)
m4_1.add_command(label="Zoom In")
m4_1.add_command(label="Zoom Out")
m4.add_cascade(label="Zoom", menu=m4_1)
m4.add_checkbutton(label="Status Bar")

menubar.add_cascade(label="View", menu=m4)

#HELP

m5= Menu(menubar, tearoff=0)
m5.add_command(label="View Help")
m5.add_command(label="Send Feedback")
m5.add_separator()
m5.add_command(label="About NoteX")

menubar.add_cascade(label="Help", menu=m5)

root.config(menu=menubar)




text= Text(root, font=("Comic Sans MS",18))
text.pack()



root.mainloop()



'''

mainmenu= Menu(root)

m1= Menu(mainmenu)

m1.add_command(label="")

mainmenu.add_cascade(label="", menu=m1)
root.config(menu=mainmenu1)


'''