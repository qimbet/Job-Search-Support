#!/usr/bin/env python3
#This is a follow-up message writer for job applications, mad-libs style. 

import os 
import datetime as dt
import pyperclip as pp
import tkinter as tk
from tkinter import font

debug = True
def d(msg):
    if debug == True:
        print(msg)


#           *************************************************************************************************************************

#                                                                            INNER PARAMETERS

#           *************************************************************************************************************************

#Colours
bgColour  = "#f1eacf"
errColour = "#ffad95"
onColour  = "#7ef191"
defaultButtonColour = "#D9D9D9"

#File Names:    ----------------------------------------------------------------------
hiringManagerFile = "Hiring_Managers"
footerFile = "Personal_Info"
identityFile = "Identity"
jobFile = "Jobs"
skillsFile = "Skills"
industriesFile = "Industries"
companiesFile = "Companies"
valuesFile = "Values"

#Folder Names
archiveFolder = "Letter_Archive"
dataFolder = "Data"


workingList = ["Hiring Manager", "Dates", "Jobs", "Identity", "Skills", "Industries", "Companies", "Values", "Titles"]
#                   0               1       2          3          4           5            6           7        8

allFilesList = [hiringManagerFile, footerFile, jobFile, identityFile, skillsFile, industriesFile, companiesFile, valuesFile]
#                   0                  1          2           3           4             5                6           7      


#Directories    ----------------------------------------------------------------------

d('PROGRAM START')

def makeFile(fileName):
    with open(f"{fileName}.txt", "a") as file:
        file.write("")

if not os.path.exists(archiveFolder):
    os.makedirs(archiveFolder)

if not os.path.exists(dataFolder):
    os.makedirs(dataFolder)

programDirectory = os.path.dirname(os.path.realpath(__file__))  
archiveDir = os.path.join(programDirectory, archiveFolder)
dataDir = os.path.join(programDirectory, dataFolder)

d(programDirectory)
os.chdir(dataDir)
d(os.getcwd())

for element in allFilesList:
    if not os.path.exists(f"{element}.txt"):
        print(f"Created new file: {element}.txt")
        makeFile(element)

#           *************************************************************************************************************************

#                                                                            GUI FUNCTIONS

#           *************************************************************************************************************************

def setFocus():
    inputField.focus_force()

def changePin(event=None):
    buttonStatus=pinWindow.get()
    if buttonStatus == True:
        root.attributes("-topmost", 1)
        setOnTopButton.config(bg=onColour, bd=5, relief="sunken")
    elif buttonStatus == False:
        root.attributes("-topmost", 0)
        setOnTopButton.config(bg=defaultButtonColour, bd=0, relief="flat")

def runProgram():
    pass

def nextStep():
    print("exiting...")
    exit()

def exitButton(event=None):
    root.quit()

#           *************************************************************************************************************************

#                                                                            BACK-END FUNCTIONS

#           *************************************************************************************************************************
def inst(message, mood=None):   #instructions. Mood sets the background colour. Note! It does not reset it afterwards
    instructions.set(message)
    if mood != None:
        instructions.config(bg=mood)

def personalInfoInput():
    popup = tk.Toplevel(root)
    popup.title("Personal Info")
    
    # Variables to store the input from the text fields
    name = tk.StringVar()
    email = tk.StringVar()
    phoneNumber = tk.StringVar()

    #Input Fields
    nameLabel = tk.Label(popup, text="Full Name:")
    nameLabel.grid(row=0, column=0, padx=10, pady=5)
    firstInput = tk.Entry(popup, textvariable=name)
    firstInput.grid(row=0, column=1, padx=10, pady=5)
    firstInput.focus_set()

    emailLabel = tk.Label(popup, text="Email:")
    emailLabel.grid(row=1, column=0, padx=10, pady=5)
    secondInput = tk.Entry(popup, textvariable=email)
    secondInput.grid(row=1, column=1, padx=10, pady=5)

    phoneNumberLabel = tk.Label(popup, text="Phone Number:")
    phoneNumberLabel.grid(row=2, column=0, padx=10, pady=5)
    thirdInput = tk.Entry(popup, textvariable=phoneNumber)
    thirdInput.grid(row=2, column=1, padx=10, pady=5)


    def saveClose(event=None):
        personalInfo = ["Name", "Email", "Phone Number"]
        personalInfo[0] = name.get()
        personalInfo[1] = email.get()
        personalInfo[2] = phoneNumber.get()
        popup.destroy()
        writeToFile(footerFile, personalInfo)

    #Save/Close Button
    saveButton = tk.Button(popup, text="Save", command=saveClose)
    saveButton.grid(row=3, columnspan=2, padx=10, pady=10)
    popup.bind("<Return>", saveClose)

def writeToFile(fileName, lst):
    with open(f'{fileName}.txt', 'w') as file:
        for element in lst:
            print(element)
            file.write(f"{element}\n")

def fileAppend(fileName, lst):
    with open(f'{fileName}.txt', 'a') as file:
        for element in lst:
            file.write(f"{element}\n")

def printListToScroll(scrollBox, lst):
    scrollBox.delete("1.0", tk.END)

    count = 0
    for element in lst:
        scrollBox.insert(tk.END, f"{count} - {element} \n")
        count += 1

def userChoiceRead(inputBox, errBox, fileName):
    lst = ftl(fileName)
    userInput = inputBox.get()
    userInput = userInput.strip()

    if userInput.isdigit():
        if (int(userInput)) <= len(lst):
            output = lst[int(userInput)-1]
            inputBox.delete(0, tk.END)
            errBox.config(bg=bgColour)
            return output
        else:
            errBox.config(bg=errColour)
            errBox.set("ERROR:\nInput not recognized! Please try again:\n")
            userChoiceRead(inputBox, errBox, fileName)                      #this should be bound to a buttonPress
    elif userInput == "":
         errBox.config(bg=bgColour)
         return "" 
    else:
        tempList = []
        tempList.append(userInput)
        fileAppend(fileName, tempList)
        inputBox.delete(0, tk.END)
        errBox.config(bg=bgColour)
        return userInput

def makeFooter ():
    footerList = ftl(footerFile)
    footer = ""
    count = 0
    for element in footerList:
        footer = footer + element +"\n"
        if count == 0: #adds a linebreak after Name
            footer = footer + "\n"
        count += 1
    return footer

def ftl(fileName): #extracts file contents into a list
    with open(f'{fileName}.txt', 'r') as file:
        allLines = []
        for line in file: 
            allLines.append(line.strip())
        return allLines

def choicePick(scrollBox, dictEntry, inputBox, errBox):  #Prompts user, and returns the string corresponding to the user's choice
    fileName = dictToFileName(dictEntry)
    lst = dictEntry[1]
    printListToScroll(scrollBox, lst)
    choice = userChoiceRead(inputBox, errBox, fileName)
    return choice

def showPrompt(dictEntry, promptField, detailsField):
    prompt = dictEntry[2][0]
    examples = "\n".join(dictEntry[2][1::])

    if len(dictEntry) <= 4: #if a substitution list exists in the Dictionary
        examples.format(tuple(dictEntry[3]))

    promptField.set(prompt)
    detailsField.set(examples)

def showChoose(dictEntry, scrollBox, inputBox, errBox, promptField, detailsField):
    global workingList
    showPrompt(dictEntry, promptField, detailsField)
    workingList[dictEntry[0]] = choicePick(scrollBox, dictEntry, inputBox, errBox)

def dictToFileName(dictEntry):
    global allFilesList
    if dictEntry[0] == 1:
        fileName =  ""
    elif dictEntry[0] == 8:
        fileName = allFilesList[2]
    else:
        fileName = allFilesList[dictEntry[0]]
    return fileName

def programSettingsInput():
    #add, remove, edit entries from lists
    #change backgrounds?
    pass


#           *************************************************************************************************************************

#                                                                            DICTIONARY: PROMPTS, MESSAGE BODY

#           *************************************************************************************************************************
if True:
    dates = [(dt.datetime.now() - dt.timedelta(days=10)).strftime("%B %d"), (dt.datetime.now() - dt.timedelta(days=7)).strftime("%B %d")]

    

    #The formatting for promptDict is a little messy. I'll break it down:
    #The dictionary associates each variable (string-named) with a list of lists:
    #   [index, [previous entries], ["prompt", *"examples"], [*substitutionsForPrompts] ]

    promptDict = {
        "Hiring Manager":   [0,
                                ftl(hiringManagerFile),    
                                ["What is the hiring manager's name?", 
                                "If you don't know, leave this section blank and press enter."]     
                            ],

        "Dates":            [1,   
                                dates,                     
                                ["When did you apply?", 
                                "The dates given here are 10 and 7 days ago, for convenience."]             
                            ],

        "Jobs":             [2,
                                ftl(jobFile),              
                                ["What's the job title?"]           
                            ],

        "Identity":         [3,
                                ftl(identityFile),         
                                ["What is your academic/professional background?", 
                                "Please include the appropriate indefinite article:", 
                                "\t_a_ university student",
                                "\t_an_ engaged member of my community"]            
                            ],

        "Skills":           [4,
                                ftl(skillsFile),           
                                ["As {}, I carry [_________] that uniquely positions me to thrive...",  
                                "a highly developed understanding of [_________]", 
                                "an aptitude in [_________]"],                         
                                [workingList[3]]
                            ],

        "Industries":       [5,
                                ftl(industriesFile),       
                                ["I carry {} that uniquely positions me to [________]", 
                                "thrive in the ________ industry", 
                                "contribute value in the role of {}"], 
                                [workingList[4], workingList[2]]
                            ], 

        "Companies":        [6,
                                ftl(companiesFile),        
                                ["What is the company name?"]     
                            ],

        "Values":           [7,
                                ftl(valuesFile),           
                                ["Why do you want to work at this specific company?", 
                                "Drawn to {} because of your [________]", 
                                "commitment to sustainability", 
                                "demonstrated support of social equity programs "], 
                                [workingList[6]]
                            ],

        "Titles":           [8,
                                ftl(jobFile),              
                                ["What title do you want to present yourself with?", 
                                "Posting is for: {}"], 
                                [workingList[2]]
                            ]
    }

    def messageBody():
        body = """Hi{},
    
    I sent in an application on {} for the advertised role of {}. I wanted to ask if you have had time to review my resume and qualifications, as well as inquire into the status of the hiring process.  

    My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As {}, I carry {} that uniquely positions me to {}.  

    Drawn to {} because of your {}, I wanted to re-express my interest in joining your team. I appreciate any information you are able to provide regarding my application, and cordially state my availability for an interview.  

    I have re-attached my resume for your convenience.

    Looking forward to hearing from you! """
        return body


#           *************************************************************************************************************************

#                                                                            GUI FORMATTING

#           *************************************************************************************************************************
if True:
    if True: #Frames and Formatting
        root = tk.Tk()
        root.title("Follow-up Generator - fugen")
        root.geometry('800x650')
        root.minsize(400, 450)
        root.configure(bg=bgColour)

        #Grid and Frame Setups
        buttonFrame = tk.Frame(root)
        buttonFrame.grid(row=0, column=2, rowspan=2, sticky="news", padx=20, pady=(25, 10))
        buttonFrame.configure(bg=bgColour)
        buttonFrame.rowconfigure(0, weight=0)

        promptFrame = tk.Frame(root)
        promptFrame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=40, pady=10)
        promptFrame.configure(bg=bgColour)

        entriesFrame = tk.Frame(root)
        entriesFrame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
        entriesFrame.columnconfigure(0, weight=1)
        entriesFrame.rowconfigure(0, weight=1)  

        textFrame = tk.Frame(root)
        textFrame.grid(row=3, column=0, columnspan=3, sticky="nesw", padx=20, pady=(5,10))
        textFrame.rowconfigure(0, weight=1)
        textFrame.columnconfigure(0,weight=1)

        root.grid_columnconfigure(0, weight=2)              
        root.grid_columnconfigure(1, weight=1)              
        root.grid_columnconfigure(2, weight=1)   

        root.grid_rowconfigure(0, weight=1)                 #Instructions; buttonFrame
        root.grid_rowconfigure(1, weight=0)                 #promptFrame
        root.grid_rowconfigure(2, weight=0)                 #Previous Entries (scrollList)
        root.grid_rowconfigure(3, weight=0, minsize=100)    #text entry 
        root.grid_rowconfigure(4, weight=0, minsize=150)    #step button

    # Text input field
    inputField = tk.Entry(textFrame, relief="sunken", justify="center")
    inputField.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    root.bind("<Return>", exitButton)
    root.after(100, setFocus())

    # Text output fields 
    instructions = tk.StringVar()
    promptDisplay = tk.StringVar()
    promptDetails = tk.StringVar()
    prevEntries = tk.StringVar()

    #Output field display labels
    instructionsCell = tk.Label(root, textvariable=instructions, relief="sunken", bd=2, wraplength=400)
    instructionsCell.grid(row=0, column=0, columnspan=2, sticky="nwse", padx=20, pady=(30,10))

    promptDisplayCell = tk.Label(promptFrame, textvariable=promptDisplay)
    promptDisplayCell.grid(row=0, sticky="nsew", padx=100, pady=10)
    boldFont = font.Font(weight="bold")
    promptDisplayCell.config(font=boldFont)

    promptDetailsCell = tk.Label(promptFrame, textvariable=promptDetails)
    promptDetailsCell.grid(row=1, sticky="nsew", padx=100, pady=10)

    root.update_idletasks()  # Update the layout
    promptDisplayCell.config(wraplength=promptFrame.winfo_width() - 120) 
    promptDetailsCell.config(wraplength=promptFrame.winfo_width() - 120) 

    prevEntriesList = tk.Listbox(entriesFrame, height =5)
    prevEntriesList.grid(row=0, column=0, sticky="nsew")
    scrollbar = tk.Scrollbar(entriesFrame)
    scrollbar.grid(row=0, column=1, sticky='ns')
    prevEntriesList.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=prevEntriesList.yview) 

    instructions.set("instructions")
    promptDisplay.set("promptDisplay")
    promptDetails.set("promptDetails")
    prevEntries.set("prevEntries")

    #Button Variables
    pinWindow = tk.BooleanVar()

    #Button definitions
    infoEditButton = tk.Button(buttonFrame, text="Edit Personal Information", command=personalInfoInput, padx = 5, pady = 5)
    programEditButton = tk.Button(buttonFrame, text="Edit Program Settings", command=programSettingsInput, padx = 5, pady = 5)
    setOnTopButton = tk.Checkbutton(buttonFrame, text="Fix Window on screen", command=changePin, padx = 5, pady = 5, variable=pinWindow, onvalue=True, offvalue=False)

    nextStepButton = tk.Button(root, text="Next Step", command=nextStep, padx = 10, pady = 15, borderwidth=5)
    nextStepButton.grid(row=4, rowspan=1, column=0, columnspan=3, sticky="nesw", padx=35, pady=35)

    infoEditButton.pack(side="top", fill="x", pady=5) 
    programEditButton.pack(side="top", fill="x", pady=5) 
    setOnTopButton.pack(side="top", fill="x", pady=5) 

#           *************************************************************************************************************************

#                                                                            MAIN

#           *************************************************************************************************************************

root.mainloop()
footer = makeFooter()
emailBody = messageBody()

for val in promptDict:
    showChoose(val, prevEntries, inputField, instructions, promptDisplay, promptDetails) #How does the 'next step' button fit in?

bodyFormatted = emailBody.format(tuple(workingList))
fullEmail = bodyFormatted + "\n\n" + footer

# print("Current letter is: \n")
# print(fullEmail + "\n\n")

os.chdir(programDirectory)
os.chdir(archiveFolder)
with open(f"Reply - {jobTitle} - {companyName}.txt", "w") as file:
    file.write(fullEmail)

os.chdir(programDirectory)
pp.copy(fullEmail)