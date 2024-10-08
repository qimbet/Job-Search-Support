#!/usr/bin/env python3
import tkinter as tk

# Dummy functions to demonstrate the logic
def func(txt):
    return (txt.upper())

def returnText():
    return "Current settings: Default"

def saveText(text):
    print(f"Saving new settings: {text}")

# Function to handle the 'Go' button click event
def handle_go():
    input_text = text_input.get()  # Get the text from input field
    result = func(input_text)      # Process the input with func
    output_var.set(result)         # Display the result in output field

# Function to handle the 'Edit Settings' button click event
def handle_edit():
    settings_text = returnText()   # Get the current settings text
    output_var.set(settings_text)  # Display the settings in the output field

    # Save the next input text after the user modifies it
    new_settings = text_input.get()
    saveText(new_settings)         # Save the new settings

def setFocus():
    text_input.focus_force()

# Initialize the main window
root = tk.Tk()
root.title("Text Processor")

# Create a text input field
text_input = tk.Entry(root, width=50)
text_input.pack(padx=10,pady=10)

root.after(100, setFocus())
# Create a variable to hold the output text
output_var = tk.StringVar()
output_var.set("Output will be displayed here.")

# Create a display label for the output
output_label = tk.Label(root, textvariable=output_var, wraplength=400)
output_label.pack(pady=10)

# Create the 'Go' button to process the input text with func()
go_button = tk.Button(root, text="Go", command=handle_go)
go_button.pack(side=tk.LEFT, padx=10)

# Create the 'Edit Settings' button to display settings and save changes
edit_button = tk.Button(root, text="Edit Settings", command=handle_edit)
edit_button.pack(side=tk.LEFT, padx=10)

# Run the main event loop
root.mainloop()
