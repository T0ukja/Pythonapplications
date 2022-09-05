import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Simple Calculator")

window.geometry("270x150")
mathnumber = ("");
show = "";
list1 = []
expression_field = Label(window, text=show )
 
expression_field.grid(columnspan=5, ipadx=70)
window.columnconfigure([0,1,2,3,4,5], minsize=50, weight=1)
def clear():
    list1.clear()
    expression_field.configure(text="")
    
def executemath():
    s = ''.join(str(x) for x in list1)
    expression_field.configure(text=eval(s))
    list1.clear()
    
def add(number,list1):

    list1 +=number
    s = ''.join(str(x) for x in list1)
    expression_field.configure(text=s)
    print(list1)

#Adding Ui for buttons (numbers and () )
one=tk.Button(master=window, text="(", command=lambda: add("(",list1))
one.grid(row=5,column=3, sticky="nsew")
one=tk.Button(master=window, text=")", command=lambda: add(")",list1))
one.grid(row=5,column=4, sticky="nsew")

one=tk.Button(master=window, text="1", command=lambda: add("1",list1))
one.grid(row=1,column=1, sticky="nsew")

two=tk.Button(master=window, text="2",command=lambda: add("2",list1))
two.grid(row=1,column=2, sticky="nsew")

three=tk.Button(master=window, text="3",command=lambda: add("3",list1))
three.grid(row=1,column=3, sticky="nsew")

four=tk.Button(master=window, text="4",command=lambda: add("4",list1))
four.grid(row=2,column=1, sticky="nsew")

five=tk.Button(master=window, text="5",command=lambda: add("5",list1))
five.grid(row=2,column=2, sticky="nsew")

six=tk.Button(master=window, text="6",command=lambda: add("6",list1))
six.grid(row=2,column=3, sticky="nsew")

seven=tk.Button(master=window, text="7",command=lambda: add("7",list1))
seven.grid(row=3,column=1, sticky="nsew")

eight=tk.Button(master=window, text="8",command=lambda: add("8",list1))
eight.grid(row=3,column=2, sticky="nsew")

nine=tk.Button(master=window, text="9",command=lambda: add("9",list1))
nine.grid(row=3,column=3, sticky="nsew")

one=tk.Button(master=window, text="Clear", command=lambda: clear())
one.grid(row=5, column=1, columnspan=2, sticky="we")

#Adding Ui for buttons (+, -, /, *)
btn_plus=tk.Button(master=window, text="+",command=lambda: add("+",list1))
btn_plus.grid(row=1,column=4, sticky="nsew")

btn_minus=tk.Button(master=window, text="-",command=lambda: add("-",list1))
btn_minus.grid(row=2,column=4, sticky="nsew")

btn_divide=tk.Button(master=window, text="/",command=lambda: add("/",list1))
btn_divide.grid(row=3,column=4, sticky="nsew")

btn_multiple=tk.Button(master=window, text="*",command=lambda: add("*",list1))
btn_multiple.grid(row=4,column=4, sticky="nsew")

btn_multiple=tk.Button(master=window, text="=", command=lambda: executemath())
btn_multiple.grid(row=4, column=1, columnspan=3, sticky="we")

tk.mainloop()


