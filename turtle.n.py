from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('My Digital Clock')
l=Label(root,font('ds-digital',80),background='black',foreground='cyan')
l.pack(anchor='center')
def time():
    string=strftime('%H:%M:%S %p')
    l.config(text=string)
    l.after(1000,time)

time()
mainloop()
