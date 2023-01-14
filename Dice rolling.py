from tkinter import * #graphical user interface
import random
root=Tk()
root.geometry('400x400')
l=Label(root,font=('Helvetica',260),bg="white",fg="red")
l.pack()
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l.config(text=f'{random.choice(dice)}')
    l.pack()

b1=Button(root,text="Roll",bg="white",fg="blue",command=roll,font=('Helvetica',20))
b1.place(x=150,y=10)
roll()

root.mainloop()



