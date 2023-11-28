import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.configure(bg="black")

# Create a function to handle button clicks
def on_click(event):
    text = event.widget.cget("text") # Get the text from the button
    if text == "=":
        try:
            expression = entry.get() # Get the expression from the entry field
            result = eval(expression) # Evaluate the expression
            entry.delete(0, tk.END) # Clear the entry field
            entry.insert(tk.END, str(result)) # Insert the result into the entry field
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input") # Show an error message
    elif text == "C": # Clear the entry field if the user clicks the "C" button
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text) # Insert the button text into the entry field


# Create an entry field for input
entry = tk.Entry(window, font=("Arial", 20), bg="black", fg="white", justify="right")
entry.pack(fill="both", expand=True, padx=10, pady=10, ipadx=10, ipady=10)

# Create buttons
button_frame = tk.Frame(window)
button_frame.pack() # Pack the frame into the window

# Create a list of buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", ".", "+",
    "="
]

for button in buttons: # Loop through the list of buttons
    b = tk.Button(button_frame, text=button, font=("Arial", 20), bg="blue", fg="white") # Create a button
    # Change C font color to red
    if button == "C":
        b.configure(fg="red")
    if button == "=":
        # Add the = button to the grid and span 4 columns
        b.grid(row=buttons.index(button) // 4, column=buttons.index(button) % 4, columnspan=4, sticky="nsew")
    else:
        # Add the button to the grid
        b.grid(row=buttons.index(button) // 4, column=buttons.index(button) % 4, sticky="nsew")
    b.bind("<Button-1>", on_click) # Bind the on_click function to the button


# Configure grid row and column weights for resizing
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
window.mainloop()
