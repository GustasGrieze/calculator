from tkinter import *
import logging

window = Tk()
user_input = StringVar()
window.geometry("650x300")

def entry_buttons():
    field_entry=field.get()
    result["text"] = field_entry

def plus():
    pass

def minus():
    pass

field = Entry(window)
button1 = Button(window, text="1", command=entry_buttons)
button1.bind("<KP_1>", lambda event: entry_buttons())
button2 = Button(window, text="2")
button3 = Button(window, text="3")
button4 = Button(window, text="4")
button5 = Button(window, text="5")
button6 = Button(window, text="6")
button7 = Button(window, text="7")
button8 = Button(window, text="8")
button9 = Button(window, text="9")
button0 = Button(window, text="0")

button_sum = Button(window, text="+")
button_minus = Button(window, text="-")
button_equals = Button(window, text="=")
result = Label(window, text="")
button1.grid(column=1, row=1)
button2.grid(column=2, row=1)
button3.grid(column=3, row=1)
button4.grid(column=1, row=2)
button5.grid(column=2, row=2)
button6.grid(column=3, row=2)
button7.grid(column=1, row=3)
button8.grid(column=2, row=3)
button9.grid(column=3, row=3)
button0.grid(column=2, row=4)

button_sum.grid(column=5, row=2)
button_minus.grid(column=5, row=3)
button_equals.grid(column=5, row=4)

field.grid(row=1)
result.grid(row=5)
window.mainloop()