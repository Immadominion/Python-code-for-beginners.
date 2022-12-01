from tkinter import *
from tkinter.ttk import *
import time
from time import strftime


def time():
    clever = strftime('%H:%M:%S:%p')
    clock.config(text=clever)
    clock.after(1000, time)


root = Tk()
root.title("CleverTime")

clock = Label(root, font=("DS-Digital.TTF", 29), background="black", foreground="red")
clock.pack(anchor='center')
clock.grid(row=2, column=1)

time()
mainloop()
