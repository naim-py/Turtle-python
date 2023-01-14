
from tkinter import *   #
from tkinter.ttk import *    #for theme sajano
from time import strftime   #time ke string a convert

root=Tk()   #Tk() function gorir window object jonne
root.title("My clock")
lebel=Label(root,font=('ds-digital',80),background='black',foreground='cyan')
lebel.pack(anchor='center')
def time():
    string=strftime('%H:%M:%S %p')
    lebel.config(text=string)
    lebel.after(1000,time)

time()
mainloop()

