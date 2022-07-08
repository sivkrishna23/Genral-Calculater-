from tkinter import *
root = Tk()
root.title("Simple Calculator")
e=Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():    
     e.delete(0,END)


def button_add():
    number = e.get()
    global first_num 
    global action
    action = 'add'
    first_num = int(number)
    e.delete(0,END)
    
    
def button_sub():
    number = e.get()
    global first_num 
    global action
    action = 'sub'
    first_num = int(number)
    e.delete(0,END)
    
    
def button_mul():
    number = e.get()
    global first_num 
    global action
    action = 'mul'
    first_num = int(number)
    e.delete(0,END)
    
    
def button_div():
    number = e.get()
    global first_num 
    global action
    action = 'div'
    first_num = int(number)
    e.delete(0,END)


def button_equal():
    sec_number = e.get()
    e.delete(0, END)
    if action == 'add':
        e.insert(0, first_num + int(sec_number))
    if action == 'sub':
        e.insert(0, first_num - int(sec_number))
    if action == 'mul':
        e.insert(0, first_num * int(sec_number))
    if action == 'div':
        e.insert(0, first_num / int(sec_number))

 
# Define Buttons

button_1 =Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 =Button(root, text="2", padx=20, pady=10, command=lambda:button_click(2))
button_3 =Button(root, text="3", padx=20, pady=10, command=lambda:button_click(3))
button_4 =Button(root, text="4", padx=20, pady=10, command=lambda:button_click(4))
button_5 =Button(root, text="5", padx=20, pady=10, command=lambda:button_click(5))
button_6 =Button(root, text="6", padx=20, pady=10, command=lambda:button_click(6))
button_7 =Button(root, text="7", padx=20, pady=10, command=lambda:button_click(7))
button_8 =Button(root, text="8", padx=20, pady=10, command=lambda:button_click(8))
button_9 =Button(root, text="9", padx=20, pady=10, command=lambda:button_click(9))
button_0 =Button(root, text="0", padx=20, pady=10, command=lambda:button_click(0))
button_add =Button(root, text="+", padx=17.5, pady=10, command=button_add)
button_sub =Button(root, text="-", padx=19, pady=10, command=button_sub)
button_mul =Button(root, text="*", padx=19, pady=10, command=button_mul)
button_div =Button(root, text="/", padx=19, pady=10, command=button_div)
button_equal =Button(root, text="=", padx=19, pady=10, command=button_equal)
button_clear =Button(root, text="C ", padx=17.5, pady=10, command=button_clear)

# Put the buttons on the screen


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div .grid(row=1, column=3)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1) 
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)


button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)



root.mainloop()

