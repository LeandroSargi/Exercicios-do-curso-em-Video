import sys
from tkinter import *


mgui = Tk()
mgui.title('Janela')
#mgui.resizable(width=False, height=False)

variavel = Label(mgui, text = 'Olá mundo!!', bg= 'yellow', fg='blue')
variavel.pack()
ent = Entry(mgui)
ent.pack()

t = Button(mgui, text= 'love', bg = 'red', fg = 'yellow')
t.pack()


mgui.mainloop()