from tkinter import *
import math

#gui interaction
window = Tk()
window.geometry("500x500")
window.title("Calculator")
window.configure(bg="sky blue")

#addding input
entry = Entry(window, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3)

#function for value to display on the entry box when clicked
def btn_clicked(value):
    number = entry.get()
    entry.delete(0, END)
    entry.insert(0, number + value)

#function for mathematical operations
def eql_clicked():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, END)
        entry.insert(0, "Error")

#clear button
def clear_clicked():
    entry.delete(0, END)

#buttons
n_btn = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "="]

for i, btn_txt in enumerate(n_btn):
    row = (i//3) + 1
    col =i%3
    if btn_txt == "=":
        button = Button (window, text=btn_txt, width=10, height=2, command=eql_clicked)
        button.grid(row=row, column=col, padx=0, pady=0)
    else:
        button = Button(window, text=btn_txt, width=10, height=2, command= lambda txt=btn_txt:btn_clicked(txt))
        button.grid(row=row, column=col, padx=0, pady=0)

clear = Button(window, text="Clear", width=10, height=2, command=clear_clicked)
clear.grid(row=6, column=0, padx=0, pady=0)

#main loop - this helps to display the window
window.mainloop()