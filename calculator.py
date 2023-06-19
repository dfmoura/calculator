import tkinter as tk

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear():
    display.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display widget
display = tk.Entry(window, width=40)
display.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
] 

row = 1
column = 0

for button in buttons:
    button_widget = tk.Button(window, text=button, width=10, height=3,
                             command=lambda value=button: button_click(value))
    button_widget.grid(row=row, column=column)
    column += 1
    if column > 3:
        column = 0
        row += 1

# Create the Clear button
clear_button = tk.Button(window, text="Clear", width=10, height=3, command=clear)
clear_button.grid(row=row, column=column)

# Create the Calculate button
calculate_button = tk.Button(window, text="Calculate", width=10, height=3, command=calculate)
calculate_button.grid(row=row, column=column+1)

# Start the main loop
window.mainloop()
