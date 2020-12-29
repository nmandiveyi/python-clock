# This is a simple algorithm for running a clock

# Import tkinter module for the gui
import tkinter as tk 

# Now import the time module
from time import strftime

def get_time():
    time_stamp = strftime('%H:%M:%S %p')
    label.config(text=time_stamp)
    label.after(1000, get_time)

# start the root window for the clock
root = tk.Tk()
root.title("Tkinter Clock")
label = tk.Label(root, font=('ds-digital', 100), background='black',foreground='white')
label.pack(anchor="center")

get_time()
root.mainloop()

