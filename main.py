# -*- encoding: utf8 -8-
from Tkinter import *
import tkMessageBox as tkmg
import tkFileDialog as tkfd
import os

def author():
    tkmg.showinfo('author','this software was created by Tianya')

def about():
    tkmg.showinfo('Copyright','this software was owned by Tianya')

def openfile():
    global filename
    filename = tkfd.askopenfilename(defaultextension = '.txt')
    if filename == '':
        filename = None
    else:
        root.title('FileNmae:'+os.path.basename(filename))
        textPad.delete(1.0,END)
        fd = open(filename,'r')
        textPad.insert(1.0,fd.read())
        fd.close()

def newfile():
    global filename
    root.title('unnamed file')
    filename = None
    textPad.delete(1.0,END)
def save():
    global filename
    try:
        fd=open(filename,'w')
        msg = textPad.get(1.0,END)
        fd.close()
    except:
        saveas()

def saveas():
    fd = tkfd.asksaveasfilename(initialfile="unnamed file.txt",defaultextension = '.txt')
    global filename
    filename = fd
    if filename == '':
        filename = None
    else:
        fd1 = open(fd,'w')
        msg =  textPad.get(1.0,END)
        fd1.write(msg)
        fd1.close()
        root.title('FileName:'+os.path.basename(fd))

def cut():
    textPad.event_generate('<<Cut>>')

def copy():
    textPad.event_generate('<<Copy>>')

def paste():
    textPad.event_generate('<<Paste>>')

def redo():
    textPad.event_generate('<<Redo>>')

def undo():
    textPad.event_generate('<<Undo>>')

root =Tk()
root.title('Node')
root.geometry('500x500+100+100')

#Create Menu
menubar = Menu(root)
root.config(menu = menubar)

#file menu
filemenu = Menu(menubar)
filemenu.add_command(label='new file',accelerator='Ctrl+N',command=newfile)
filemenu.add_command(label='open file',accelerator = 'Ctrl + O',command=openfile)
filemenu.add_command(label='save file',accelerator = 'Ctrl + S',command=save)
filemenu.add_command(label='save as file',accelerator = 'Ctrl + Shift + S',command=saveas)
menubar.add_cascade(label='file',menu=filemenu)

#edit menu
editmenu= Menu(menubar)
editmenu.add_command(label='undo',accelerator='Ctrl+Z',command=undo)
editmenu.add_command(label='redo',accelerator='Ctrl+Y',command=redo)
editmenu.add_separator()
editmenu.add_command(label='cut',accelerator='Ctrl+X',command=cut)
editmenu.add_command(label='copy',accelerator='Ctrl+C',command=copy)
editmenu.add_command(label='paste',accelerator='Ctrl+V',command=paste)
editmenu.add_separator()
editmenu.add_command(label='find',accelerator='Ctrl+F')
editmenu.add_command(label='select',accelerator='Ctrl+A')
menubar.add_cascade(label='edit',menu=editmenu)

#about menu
aboutmenu = Menu(menubar)
aboutmenu.add_command(label='author',command=author)
aboutmenu.add_command(label='copyright',command=about)
menubar.add_cascade(label='about',menu=aboutmenu)

#toolbar
toolbar = Frame(root,height=25,bg='light sea green')
shortButton = Button(toolbar,text = 'open', command=openfile)
shortButton.pack(side=LEFT,padx = 5,pady = 5)
shortButton = Button(toolbar,text = 'save')
shortButton.pack(side=LEFT,padx = 5,pady = 5)
toolbar.pack(fill=X,expand=NO)

#Status Bar
status = Label(root,text = 'Ln20',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

#linenumber&test
lnlabel=Label(root,width=2,bg='antique white')
lnlabel.pack(side=LEFT,fill = Y)

textPad= Text(root,undo=True)
textPad.pack(expand=YES,fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT,fill=Y)
root.mainloop()