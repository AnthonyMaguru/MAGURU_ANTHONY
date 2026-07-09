from tkinter import *

def add():
    result.config(text=float(num1.get()) + float(num2.get()))

def subtract():
    result.config(text=float(num1.get()) - float(num2.get()))

def multiply():
    result.config(text=float(num1.get()) * float(num2.get()))

def divide():
    if float(num2.get()) == 0:
        result.config(text="Cannot divide by zero")
    else:
        result.config(text=float(num1.get()) / float(num2.get()))

root = Tk()
root.title("Calculator")

Label(root, text="First Number").grid(row=0, column=0)
num1 = Entry(root)
num1.grid(row=0, column=1)

Label(root, text="Second Number").grid(row=1, column=0)
num2 = Entry(root)
num2.grid(row=1, column=1)

Button(root, text="Add", command=add).grid(row=2, column=0)
Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
Button(root, text="Divide", command=divide).grid(row=3, column=1)

result = Label(root, text="Result")
result.grid(row=4, column=0, columnspan=2)

root.mainloop()