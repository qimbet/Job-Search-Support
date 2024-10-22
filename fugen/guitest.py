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


#           *************************************************************************************************************************

#                                                                            GUI FUNCTIONS

#           *************************************************************************************************************************

if True:
    def printToDisplay(outputField, *text):
        allInputs = []
        for line in text:
            allInputs.append(line)

        delim = "\n"
        allLinesInOne = delim.join(text)
        outputField.set(allLinesInOne)

    def setFocus():
        inputField.focus_force()

    def editPersonalInfo():
        pass

    def editProgramInfo():
        pass
    
    def runProgram():
        pass

    def nextStep():
        if True: 
            print("exiting...")
            exit()

    def exitButton(event=None):
        root.quit()




#           *************************************************************************************************************************

#                                                                            GUI SETUP

#           *************************************************************************************************************************
root = tk.Tk()
root.title("Follow-up Generator")
root.geometry('800x650')
root.minsize(300, 150)
root.configure(bg="#f1eacf")

#Grid Setup
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)

# Create a text input field
inputField = tk.Entry(root)
inputField.grid(row=5, column=0, columnspan=3, sticky="nesw", padx=20, pady=5)

#inputField.bind("<Return>", nextStep)
root.bind("<Return>", exitButton)

root.after(100, setFocus())

# Text output fields 
instructions = tk.StringVar()
promptDisplay = tk.StringVar()
promptDetails = tk.StringVar()
prevEntries = tk.StringVar()
stepButtonLabel = tk.StringVar()

#Output field display labels
instructionsCell = tk.Label(root, textvariable=instructions, wraplength=400)
instructionsCell.grid(row=0, column=0, columnspan=2, sticky="nw", padx=10, pady=10)

promptDisplayCell = tk.Label(root, textvariable=promptDisplay, wraplength=400)
promptDisplayCell.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

promptDetailsCell = tk.Label(root, textvariable=promptDetails, wraplength=400)
promptDetailsCell.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

prevEntriesCell = tk.Label(root, textvariable=prevEntries, wraplength=400)
prevEntriesCell.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

stepButtonLabelCell = tk.Label(root, textvariable=stepButtonLabel, wraplength=400)
stepButtonLabelCell.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

instructions.set("Instructions cell")
promptDisplay.set("Prompt Display")
promptDetails.set("Prompt Details")
prevEntries.set("Previous Entries (archive)")
stepButtonLabel.set("Button Label")


#Button definitions
infoEditButton = tk.Button(root, text="Edit Personal Information", command=editPersonalInfo, padx = 5, pady = 5)
programEditButton = tk.Button(root, text="Edit Program Information", command=editProgramInfo, padx = 5, pady = 5)
#runProgramButton = tk.Button(root, text="Generate Follow-up Email", command=runProgram)
nextStepButton = tk.Button(root, text="Next Step", command=nextStep, padx = 10, pady = 15, borderwidth=5)

infoEditButton.grid(row=0, column=2, sticky="ne", padx=10, pady=10)     
programEditButton.grid(row=1, column=2, sticky="ne", padx=10, pady=10)
#runProgramButton.pack(side=tk.LEFT, expand=True, padx=10)
nextStepButton.grid(row=6, rowspan=1, column=0, columnspan=3, sticky="nesw", padx=35, pady=35)

#BEGIN MAIN 
#

root.mainloop()


#tk object usage examples
#promptReader.set("Output will be displayed here.")
#x = inputField.get()