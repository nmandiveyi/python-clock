# This is a simple algorithm for running a clock

# Import tkinter module for the gui
from tkinter import *
from tkinter.ttk import *

# Now import the time module
from time import strftime

def get_time():
    time_stamp = strftime('%H:%M:%S %p')
    label.config(text=time_stamp)
    label.after(1000, get_time)

# start the root window for the clock
root = Tk()
label = Label(root, font=('ds-digital', 100), bg='black',fg='white')
label.pack(ANCHOR="center")

