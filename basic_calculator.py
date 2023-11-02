from tkinter import *

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    current_text = entry.get()
    if text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, text)

# Creating the main application window
root = Tk()
root.title("Calculator")
root.configure(bg="black")  # Set background color to black

# Configuring the input field to span the entire width with increased padding
entry = Entry(root, font=("Arial", 18, "bold"), bd=10, insertwidth=4, width=24, borderwidth=4, justify='right', bg="white")
entry.grid(row=0, column=0, columnspan=4, padx=(20, 10), pady=(20, 10), ipady=15)  # Increased internal padding for the display

# Button layout as per your request
button_layout = [
    'C', '(', ')', '%',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '=', '0', '.', '+'
]

row_val = 1
col_val = 0

for button in button_layout:
    if button == 'C':
        button_frame = Button(root, text=button, font=("Arial", 18, "bold"), width=8, bg='red')
    elif button == '=':
        button_frame = Button(root, text=button, font=("Arial", 18, "bold"), width=8, bg='green')
    elif button in ['(', ')', '%', '/', '*', '-', '+', '.']:
        button_frame = Button(root, text=button, font=("Arial", 18, "bold"), width=8, bg='white')
    else:
        button_frame = Button(root, text=button, font=("Arial", 18, "bold"), width=8, bg='gray')
    button_frame.grid(row=row_val, column=col_val, padx=10, pady=10)
    button_frame.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Running the main loop
root.mainloop()
