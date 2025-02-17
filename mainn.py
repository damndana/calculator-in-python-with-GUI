from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

light_mode = {
    "bg": "white",
    "fg": "black",
    "button_bg": "light gray",
    "button_fg": "black",
    "special_bg": "orange",
    "special_fg": "black",
    "entry_bg": "white",
    "entry_fg": "black"
}

dark_mode = {
    "bg": "black",
    "fg": "white",
    "button_bg": "dark gray",
    "button_fg": "black",
    "special_bg": "dark orange",
    "special_fg": "black",
    "entry_bg": "white",
    "entry_fg": "black"
}

current_mode = light_mode

def toggle_mode():
    global current_mode
    current_mode = dark_mode if current_mode == light_mode else light_mode
    
    root.config(bg=current_mode["bg"])
    e.config(bg=current_mode["entry_bg"], fg=current_mode["entry_fg"])
    button_1.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_2.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_3.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_4.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_5.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_6.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_7.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_8.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_9.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_0.config(bg=current_mode["button_bg"], fg=current_mode["button_fg"])
    button_add.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])
    button_subtract.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])
    button_multiply.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])
    button_divide.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])
    button_equal.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])
    button_clear.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])
    toggle_button.config(bg=current_mode["special_bg"], fg=current_mode["special_fg"])

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))
    elif math == "division":
        e.insert(0, f_num / float(second_number))

# Define buttons
button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

toggle_button = Button(root, text="Mode", padx=10, pady=10, command=toggle_mode)

button_add = Button(root, text="+", padx=20, pady=20, command=button_add, bg=light_mode["special_bg"], fg=light_mode["special_fg"])
button_equal = Button(root, text="=", padx=20, pady=20, command=button_equal, bg=light_mode["special_bg"], fg=light_mode["special_fg"])
button_clear = Button(root, text="C", padx=20, pady=20, command=button_clear, bg=light_mode["special_bg"], fg=light_mode["special_fg"])
button_divide = Button(root, text="/", padx=20, pady=20, command=button_divide, bg=light_mode["special_bg"], fg=light_mode["special_fg"])
button_multiply = Button(root, text="*", padx=20, pady=20, command=button_multiply, bg=light_mode["special_bg"], fg=light_mode["special_fg"])
button_subtract = Button(root, text="-", padx=20, pady=20, command=button_subtract, bg=light_mode["special_bg"], fg=light_mode["special_fg"])

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_clear.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=0)
toggle_button.grid(row=0, column=3)

root.mainloop()
