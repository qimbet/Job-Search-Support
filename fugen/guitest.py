#!/usr/bin/env python3
import tkinter as tk
#import fugen as fg

#GUI Objects:
#   BUTTONS:
#   infoEdit        - Edit personal info          
#   programEdit     - Allows users to add, remove, and edit archived entries
#   runProgram      - Generate Follow-up Email
#   nextStep        - Move to the next madLib. On last step, replace with "runProgram" button
#
#   OUTPUT FIELDS: 
#   instructions    - Shows immediately applicable instructions
#   promptDisplay   - Shows the prompt for input 
#   promptDetails   - Shows further information about the prompt (i.e. examples)
#   prevEntries     - SCROLL LIST - Shows Previous entry data from which a user can choose
#
#   INPUT FIELDS: 
#   choiceIn        - SIZE LIMITED - Text field in which a user can enter their selection choice, or type a new entry.
#
#


if True:
    def func(txt):
        return (txt.upper())

    def saveText(text):
        print(f"Text registered as input: {text}")

    def valConfirm():
        inputText = inputField.get()  # Get the text from input field
        result = func(inputText)      # Process the input with func
        print(f"Text interpreted, passed through a function")
        optionsReader.set(result)      

    # Function to handle the 'Edit Settings' button click event
    def handle_edit(prompt):
        optionsReader.set(prompt)  # Display the settings in the output field

        # Save the next input text after the user modifies it
        new_settings = inputField.get()
        saveText(new_settings)         # Save the new settings

    def setFocus():
        inputField.focus_force()

    def editPersonalInfo():
        pass

    def editProgramInfo():
        pass
    
    def runProgram():
        pass

    def nextStep():
        pass

# Initialize the main window
root = tk.Tk()
root.title("Follow-up Generator")
root.geometry('800x650')
root.configure(bg="#f1eacf")

# Create a text input field
inputField = tk.Entry(root)
inputField.pack(side=tk.BOTTOM, fill=tk.X, expand=True, padx=10,pady=10)
inputField.bind("<Return>", valConfirm())

root.after(100, setFocus())

# Text output fields 
instructions = tk.StringVar()
promptDisplay = tk.StringVar()
promptDetails = tk.StringVar()
prevEntries = tk.StringVar()
stepButtonLabel = tk.StringVar()

#Output field display labels
instructionsCell = tk.Label(root, textvariable=instructions, wraplength=400)
instructionsCell.pack(pady=10)

promptDisplayCell = tk.Label(root, textvariable=promptDisplay, wraplength=400)
promptDisplayCell.pack(pady=10)

promptDetailsCell = tk.Label(root, textvariable=promptDetails, wraplength=400)
promptDetailsCell.pack(pady=10)

prevEntriesCell = tk.Label(root, textvariable=prevEntries, wraplength=400)
prevEntriesCell.pack(pady=10)

stepButonLabelCell = tk.Label(root, textvariable=stepButtonLabel, wraplength=400)
stepButtonLabelCell.pack(pady=25)


#Button definitions
infoEditButton = tk.Button(root, text="Edit Personal Information", command=editPersonalInfo)
programEditButton = tk.Button(root, text="Edit Program Information", command=editProgramInfo)
runProgramButton = tk.Button(root, text="Generate Follow-up Email", command=runProgram)
nextStepButton = tk.Button(root, text="Next Step", command=nextStep)

infoEditButton.pack(side=tk.RIGHT, expand=False, padx=10)     #Adjust spacing to fit UI
programEditButton.pack(side=tk.RIGHT, expand=False, padx=10)
runProgramButton.pack(side=tk.LEFT, expand=True, padx=10)
nextStepButton.pack(side=tk.LEFT, expand=True, padx=10)

#####Experimentation 
instructions = tk.StringVar()
instructionsCell = tk.Label(root, textvariable=instructions, wraplength=400)
instructionsCell.pack(pady=10)



# Run the main event loop
root.mainloop()


#tk object usage examples
#promptReader.set("Output will be displayed here.")