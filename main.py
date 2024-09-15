from tkinter import *
from calculator import Calculator

window = Tk()
window.config(padx=10, pady=10)
window.title("")

calculator = Calculator(window)

window.mainloop()