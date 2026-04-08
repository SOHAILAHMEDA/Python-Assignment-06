from tkinter import *

window = Tk()
window.geometry("350x400")

# Entry box to display numbers and operation.
entry = Entry(window, width = 40, borderwidth= 5)
entry.place(x = 50, y = 0)

def click(num):
    result = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(result) + str(num))

# Buttons for numbers and operation.
b = Button(window, text="1", width=12, command= lambda:click(1))
b.place(x = 20, y = 60)

b = Button(window, text="2", width=12, command= lambda:click(2))
b.place(x = 120, y = 60)

b = Button(window, text="3", width=12, command= lambda:click(3))
b.place(x = 220, y = 60)

b = Button(window, text="4", width=12, command= lambda:click(4))
b.place(x = 20, y = 120)

b = Button(window, text="5", width=12, command= lambda:click(5))
b.place(x = 120, y = 120)

b = Button(window, text="6", width=12, command= lambda:click(6))
b.place(x = 220, y = 120)

b = Button(window, text="7", width=12, command= lambda:click(7))
b.place(x = 20, y = 180)

b = Button(window, text="8", width=12, command= lambda:click(8))
b.place(x = 120, y = 180)

b = Button(window, text="9", width=12, command= lambda:click(9))
b.place(x = 220, y = 180)

b = Button(window, text="0", width=12, command= lambda:click(0))
b.place(x = 20, y = 240)

def add():
    n1 = entry.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entry.delete(0, END)

b = Button(window, text="+", width=12, command=add)
b.place(x = 120, y = 240)

def sub():
    n1 = entry.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    entry.delete(0, END)

b = Button(window, text="-", width=12, command=sub)
b.place(x = 220, y = 240)

def mul():
    n1 = entry.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    entry.delete(0, END)

b = Button(window, text="*", width=12, command=mul)
b.place(x = 20, y = 300)

def div():
    n1 = entry.get()
    global math
    math = "division"
    global i
    i = int(n1)
    entry.delete(0, END)

b = Button(window, text="/", width=12, command=div)
b.place(x = 120, y = 300)

def equal():
    n2 = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, str(i + int(n2)))
    elif math == "subtraction":
        entry.insert(0, str(i - int(n2)))
    elif math == "multiplication":
        entry.insert(0, str(i * int(n2)))
    elif math == "division":
        if int(n2) == 0:
            entry.insert(0, f"Cannot divide {i} by 0")
        else:
            entry.insert(0, str(i / int(n2)))

b = Button(window, text="=", width=12, command=equal)
b.place(x = 220, y = 300)

def clear():
    entry.delete(0, END)

b = Button(window, text="clear", width=12, command=clear)
b.place(x = 20, y = 360)

window.mainloop()
