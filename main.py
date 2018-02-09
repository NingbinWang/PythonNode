from Tkinter import *
# -*- encoding: utf8 -8-

root =Tk()
root.title('Node')
root.geometry('500x500+100+100')

#Create Menu
menubar = Menu(root)
root.config(menu = menubar)

#file menu
filemenu = Menu(menubar)
filemenu.add_command(label='new file',accelerator='Ctrl+N')
filemenu.add_command(label='open file',accelerator = 'Ctrl + O')
filemenu.add_command(label='save file',accelerator = 'Ctrl + S')
filemenu.add_command(label='save as file',accelerator = 'Ctrl + Shift + S')
menubar.add_cascade(label='file',menu=filemenu)

#edit menu
editmenu= Menu(menubar)
editmenu.add_command(label='undo',accelerator='Ctrl+Z')
editmenu.add_command(label='rset',accelerator='Ctrl+Y')
editmenu.add_separator()
editmenu.add_command(label='shear',accelerator='Ctrl+X')
editmenu.add_command(label='copy',accelerator='Ctrl+C')
editmenu.add_command(label='paste',accelerator='Ctrl+V')
editmenu.add_separator()
editmenu.add_command(label='find',accelerator='Ctrl+F')
editmenu.add_command(label='select',accelerator='Ctrl+A')
menubar.add_cascade(label='edit',menu=editmenu)

#about menu
aboutmenu = Menu(menubar)
aboutmenu.add_command(label='author')
aboutmenu.add_command(label='copyright')
menubar.add_cascade(label='about',menu=aboutmenu)

#toolbar
toolbar = Frame(root,height=25,bg='light sea green')
shortButton = Button(toolbar,text = 'open')
shortButton.pack(side=LEFT,padx = 5,pady = 5)

shortButton = Button(toolbar,text = 'save')
shortButton.pack(side=LEFT,padx = 5,pady = 5)

toolbar.pack(fill=X,expand=NO)

root.mainloop()