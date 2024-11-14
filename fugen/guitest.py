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
    
    def changePin(event=None):
        # global pinTop = False
        # root.attributes("-topmost", True)
        pass




#           *************************************************************************************************************************

#                                                                            GUI SETUP

#           *************************************************************************************************************************
root = tk.Tk()
root.title("Follow-up Generator - GUItest")
root.geometry('800x600')
root.minsize(200, 40)
root.configure(bg="#f1eacf")

#Grid Setup
buttonFrame = tk.Frame(root)
buttonFrame.grid(row=0, column=2, rowspan=2, sticky="news", padx=20, pady=20)

root.grid_columnconfigure(0, weight=1, minsize=150)              
root.grid_columnconfigure(1, weight=0)              
root.grid_columnconfigure(2, weight=0)              
root.grid_rowconfigure(0, weight=1)                 #Personal Info
root.grid_rowconfigure(1, weight=1, minsize=55)     #Program Settings
root.grid_rowconfigure(2, weight=0)                 #Prompt Display
root.grid_rowconfigure(3, weight=1)                 #Prompt Details
root.grid_rowconfigure(4, weight=0)                 #Previous Entries
root.grid_rowconfigure(5, weight=0, minsize=150)    #text entry 
root.grid_rowconfigure(6, weight=0, minsize=150)    #step button

# Create a text input field
inputField = tk.Entry(root, relief="sunken", justify="center")
inputField.grid(row=5, column=0, columnspan=3, sticky="nesw", padx=20, pady=(15,10))

root.bind("<Return>", exitButton)
root.after(100, setFocus())

# Text output fields 
instructions = tk.StringVar()
promptDisplay = tk.StringVar()
promptDetails = tk.StringVar()
prevEntries = tk.StringVar()

#Output field display labels
instructionsCell = tk.Label(root, textvariable=instructions, wraplength=400)
instructionsCell.grid(row=0, column=0, columnspan=2, sticky="nw", padx=10, pady=10)

promptDisplayCell = tk.Label(root, textvariable=promptDisplay, wraplength=400)
promptDisplayCell.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

promptDetailsCell = tk.Label(root, textvariable=promptDetails, wraplength=400)
promptDetailsCell.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

prevEntriesCell = tk.Label(root, textvariable=prevEntries, wraplength=400)
prevEntriesCell.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

instructions.set("Instructions cell")
promptDisplay.set("Prompt Display")
promptDetails.set("Prompt Details")
prevEntries.set("Previous Entries (archive)")

#Button definitions
infoEditButton = tk.Button(buttonFrame, text="Edit Personal Information", command=editPersonalInfo, padx = 5, pady = 5)
programEditButton = tk.Button(buttonFrame, text="Edit Program Settings", command=editProgramInfo, padx = 5, pady = 5)
setOnTopButton = tk.Checkbutton(buttonFrame, text="Fix Window on screen", command=changePin, padx = 5, pady = 5)

nextStepButton = tk.Button(root, text="Next Step", command=nextStep, padx = 10, pady = 15, borderwidth=5)

# infoEditButton.grid(row=0, column=2, sticky="ew", padx=(350, 10), pady=10)     
# programEditButton.grid(row=1, column=2, sticky="new", padx=(350, 10), pady=10)
# setOnTopButton.grid(row=1, column=2, sticky="sew", padx=(350, 10), pady=10)    

nextStepButton.grid(row=6, rowspan=1, column=0, columnspan=3, sticky="nesw", padx=35, pady=35)

infoEditButton.pack(side="top", fill="x", pady=5) 
programEditButton.pack(side="top", fill="x", pady=5) 
setOnTopButton.pack(side="top", fill="x", pady=5) 

#BEGIN MAIN 
#

root.mainloop()


#tk object usage examples
#promptReader.set("Output will be displayed here.")
#x = inputField.get()