__author__ = 'Paul'

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too

top = Tk()
# Code to add widgets will go here...
top.mainloop()
