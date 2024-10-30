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
successColour = "#6BF77D"
defaultButtonColour = "#D9D9D9"
coloursList = [bgColour, errColour, onColour, defaultButtonColour]

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



workingListHardcoded = ["Hiring Manager", "Dates", "Jobs", "Identity", "Skills", "Industries", "Companies", "Values", "Titles"] #Used only to reset workingList at the end of the loop
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

#os.chdir(programDirectory)

#           *************************************************************************************************************************

#                                                                            TKINTER CLASSES

#           *************************************************************************************************************************
class fugenMain:
    def __init__(self, rootIn, bgColour, coloursList):
        self.currentStep = 0
        self.emailFinal = ""

        bgColour = coloursList[0]
        errColour = coloursList[1]
        onColour = coloursList[2]
        defaultButtonColour = coloursList[3]

        self.root = rootIn
        root.title("Follow-up Generator - fugen")
        self.footer = makeFooter(footerFile)
        if True: #Frames and Formatting
            self.root.geometry('800x650')
            self.root.minsize(400, 450)
            self.root.configure(bg=self.bgColour)

            #Grid and Frame Setups
            buttonFrame = tk.Frame(self.root)
            buttonFrame.grid(row=0, column=2, rowspan=2, sticky="news", padx=20, pady=(25, 10))
            buttonFrame.configure(bg=self.bgColour)
            buttonFrame.rowconfigure(0, weight=0)

            promptFrame = tk.Frame(self.root)
            promptFrame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=40, pady=10)
            promptFrame.configure(bg=bgColour)

            entriesFrame = tk.Frame(self.root)
            entriesFrame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
            entriesFrame.columnconfigure(0, weight=1)
            entriesFrame.rowconfigure(0, weight=1)  

            textFrame = tk.Frame(self.root)
            textFrame.grid(row=3, column=0, columnspan=3, sticky="nesw", padx=20, pady=(5,10))
            textFrame.rowconfigure(0, weight=1)
            textFrame.columnconfigure(0,weight=1)

            self.root.grid_columnconfigure(0, weight=2)              
            self.root.grid_columnconfigure(1, weight=1)              
            self.root.grid_columnconfigure(2, weight=1)   

            self.root.grid_rowconfigure(0, weight=1)                 #Instructions; buttonFrame
            self.root.grid_rowconfigure(1, weight=0)                 #promptFrame
            self.root.grid_rowconfigure(2, weight=0)                 #Previous Entries (scrollList)
            self.root.grid_rowconfigure(3, weight=0, minsize=100)    #text entry 
            self.root.grid_rowconfigure(4, weight=0, minsize=150)    #step button

        # Text input field
        self.inputField = tk.Entry(self.textFrame, relief="sunken", justify="center")
        self.inputField.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Text output fields 
        self.instructions = tk.StringVar()
        self.promptDisplay = tk.StringVar()
        self.promptDetails = tk.StringVar()
        self.prevEntries = tk.StringVar()

        #Output field display labels
        self.instructionsCell = tk.Label(self.root, textvariable=self.instructions, relief="sunken", bd=2, wraplength=400)
        self.instructionsCell.grid(row=0, column=0, columnspan=2, sticky="nwse", padx=20, pady=(30,10))

        self.promptDisplayCell = tk.Label(self.promptFrame, textvariable=self.promptDisplay)
        self.promptDisplayCell.grid(row=0, sticky="nsew", padx=100, pady=10)
        boldFont = font.Font(weight="bold")
        self.promptDisplayCell.config(font=boldFont)

        self.promptDetailsCell = tk.Label(self.promptFrame, textvariable=self.promptDetails)
        self.promptDetailsCell.grid(row=1, sticky="nsew", padx=100, pady=10)

        self.root.update_idletasks()  # Update the layout
        self.promptDisplayCell.config(wraplength=self.promptFrame.winfo_width() - 120) 
        self.promptDetailsCell.config(wraplength=self.promptFrame.winfo_width() - 120) 

        self.prevEntriesList = tk.Listbox(self.entriesFrame, height =5)
        self.prevEntriesList.grid(row=0, column=0, sticky="nsew")
        self.scrollbar = tk.Scrollbar(self.entriesFrame)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.prevEntriesList.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.prevEntriesList.yview) 

        self.instructions.set("instructions go here")
        self.promptDisplay.set(promptDict[workingListHardcoded[self.currentStep]][2][0]) #currentStep == 0 at program start. Used text for readability
        self.promptDetails.set(promptDict[workingListHardcoded[self.currentStep]][2][1::])
        self.prevEntries.set(promptDict[workingListHardcoded[self.currentStep]][1][0::])

        #Window-state Variables
        self.pinWindow = tk.BooleanVar()

        #Button definitions
        self.infoEditButton = tk.Button(self.buttonFrame, text="Edit Personal Information", command=self.PIPopup, padx = 5, pady = 5)
        self.programEditButton = tk.Button(self.buttonFrame, text="Edit Program Settings", command=self.programSettingsInput, padx = 5, pady = 5)
        self.setOnTopButton = tk.Checkbutton(self.buttonFrame, text="Fix Window on screen", command=self.changePin, padx = 5, pady = 5, variable=self.pinWindow, onvalue=True, offvalue=False)

        self.infoEditButton.pack(side="top", fill="x", pady=5) 
        self.programEditButton.pack(side="top", fill="x", pady=5) 
        self.setOnTopButton.pack(side="top", fill="x", pady=5) 

        self.nextStepButton = tk.Button(self.root, text="Next Step", command=lambda: self.saveCont(promptDict[workingListHardcoded[self.currentStep]]), padx = 10, pady = 15, borderwidth=5)
        self.nextStepButton.grid(row=4, rowspan=1, column=0, columnspan=3, sticky="nesw", padx=35, pady=35)
        self.root.bind("<Return>", lambda event: self.nextStepButton.invoke())
       
        self.root.after(100, self.setFocus())
        

    def PIPopup(self): #Creates an instance of personalInfoPopup as a child of root
        parentWindow = tk.Toplevel(self.root)
        personalInfoPopup(parentWindow)
        self.footer = makeFooter(footerFile)

    def changePin(self, event=None):
        buttonStatus=self.pinWindow.get()
        if buttonStatus == True:
            self.root.attributes("-topmost", 1)
            self.setOnTopButton.config(bg=self.onColour, bd=5, relief="sunken")
        elif buttonStatus == False:
            root.attributes("-topmost", 0)
            self.setOnTopButton.config(bg=self.defaultButtonColour, bd=0, relief="flat")

    def setFocus(self):
        self.inputField.focus_force()

    def inst(self, message, mood=None):   #instructions. Mood sets the background colour. Note! It does not reset it afterwards
        self.instructions.set(message)
        if mood != None:
            self.instructions.config(bg=mood)

    def printListToScroll(self, lst):
        self.inputClear()
        count = 0
        for element in lst:
            self.prevEntries.insert(tk.END, f"{count}\t- {element} \n")
            count += 1
    
    def inputClear(self, err=None): 
        self.inputField.delete(0, tk.END)
        if err == None:                             #Not sure if this is valid, but it's worth a try
            self.instructions.config(bg=bgColour)

    def userChoiceRead(self, dictEntry): #reads input, bound-checks integers. Outputs int() for a select value, "", or str() as appropriate. Variable return type!
        fileName = dictToFileName(dictEntry)
        lstLen = len(ftl(fileName))
        userInput = self.inputField.get()
        userInput = userInput.strip()

        if userInput.isdigit():
            userInput = int(userInput)
            if (userInput) <= lstLen:
                return (userInput-1)
            else:
                inst("ERROR:\nThe value you entered is not within bounds! \nPlease try again.", errColour)
                inputClear(True) #Passing any value to inputClear() indicates error status, and does not reset the colour in Instructions
                return False
        elif userInput == "":
            return userInput 
        else: #Custom/new user entry
            fileAppend(fileName, userInput)
            return userInput

    def saveCont(self, dictEntry): #saves a valid choice into memory, steps forward in program execution. Updates prompts         
        global workingList
        fileName = dictToFileName(dictEntry)
        choice = userChoiceRead(fileName)

        if choice != False: #choice should be str, "", or int. 'False' denotes an error!                        
            if type(choice)== int:
                choice = intToEntry(fileName, choice) #converts an integer choice into the desired string
            saveInput(choice)
            if (self.currentStep == 8):
                self.finalize()
            else:
                self.currentStep = self.currentStep + 1
                showPrompt(dictEntry[workingListHardcoded[self.currentStep]])
                
        else: 
            self.inst("Something's wrong! saveCont is receiving a false value from userChoiceRead", errColour)
            exit() #%dunno how I feel about including an exit statement here
            
        #%return choice might not be the best approach. This should be the step that stores values and increments currentStep
    
    def saveInput(userInput):
        global workingList
        workingList[self.currentStep] = userInput

    def showPrompt(self, dictEntry):
        prompt = dictEntry[2][0]
        examples = "\n".join(dictEntry[2][1::])

        if len(dictEntry) >= 4: #if a substitution list exists in the Dictionary
            examples = examples.format(tuple(dictEntry[3]))

        self.promptDisplay.set(prompt)
        self.promptDetails.set(examples)

    def finalize(self):
        self.buildLetter()
        self.copyMail()
        
    def buildLetter(self):
        self.emailFinal
        def messageBody():
            body = """Hi{},
        
        I sent in an application on {} for the advertised role of {}. I wanted to ask if you have had time to review my resume and qualifications, as well as inquire into the status of the hiring process.  

        My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As {}, I carry {} that uniquely positions me to {}.  

        Drawn to {} because of your {}, I wanted to re-express my interest in joining your team. I appreciate any information you are able to provide regarding my application, and cordially state my availability for an interview.  

        I have re-attached my resume for your convenience.

        Looking forward to hearing from you! """
            return body
        emailBody = messageBody()
        self.emailFinal = (emailBody.format(*workingList)) + "\n\n" + self.footer

    def copyMail(self): #saves letter, copies it, and resets program to start
        pp.copy(self.emailFinal)
        inst("Follow-up email generated!\nIt's been copied into your computer's memory.\nPress ctrl+v / cmd+v to paste it :)", successColour)
        os.chdir(archiveDir)
        with open(f"Reply - {workingList[2]} - {workingList[6]}.txt", "w") as file:
            file.write(fullEmail)
        os.chdir(dataDir)
        workingList = workingListHardcoded
        self.currentStep = 0
        # fakeList = [self.emailFinal]
        # self.printListToScroll(fakeList)

    def programSettingsInput(self):     #%NOT DONE!
        #add, remove, edit entries from lists
        #change backgrounds?
        pass

class personalInfoPopup:
    def __init__(self, root):
        self.popup = root
        self.popup.title("Personal Info")
        
        # Variables to store the input from the text fields
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.phoneNumber = tk.StringVar()

        #Input Fields
        nameLabel = tk.Label(self.popup, text="Full Name:")
        nameLabel.grid(row=0, column=0, padx=10, pady=5)
        firstInput = tk.Entry(self.popup, textvariable=self.name)
        firstInput.grid(row=0, column=1, padx=10, pady=5)
        firstInput.focus_set()

        emailLabel = tk.Label(self.popup, text="Email:")
        emailLabel.grid(row=1, column=0, padx=10, pady=5)
        secondInput = tk.Entry(self.popup, textvariable=self.email)
        secondInput.grid(row=1, column=1, padx=10, pady=5)

        phoneNumberLabel = tk.Label(self.popup, text="Phone Number:")
        phoneNumberLabel.grid(row=2, column=0, padx=10, pady=5)
        thirdInput = tk.Entry(self.popup, textvariable=self.phoneNumber)
        thirdInput.grid(row=2, column=1, padx=10, pady=5)

            #Save/Close Button
        saveButton = tk.Button(self.popup, text="Save", command=self.saveClose)
        saveButton.grid(row=3, columnspan=2, padx=10, pady=10)
        self.popup.bind("<Return>", self.saveClose)


    def saveClose(self, event=None):
        self.personalInfo = ["Name", "Email", "Phone Number"]
        self.personalInfo[0] = self.name.get()
        self.personalInfo[1] = self.email.get()
        self.personalInfo[2] = self.phoneNumber.get()
        writeToFile(footerFile, self.personalInfo)
        
        self.popup.destroy()
        


        
#           *************************************************************************************************************************

#                                                                            FILE-HANDLING FUNCTIONS

#           *************************************************************************************************************************

def writeToFile(fileName, lst):
    with open(f'{fileName}.txt', 'w') as file:
        for element in lst:
            print(element)
            file.write(f"{element}\n")

def fileAppend(fileName, val):
    with open(f'{fileName}.txt', 'a') as file:
        file.write(f"{val}\n")          #%is it known that append does not include newlines by default?

def makeFooter(footerFile):
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

def dictToFileName(dictEntry): #takes a dictionary key as argument
    global allFilesList
    if dictEntry[0] == 1: #Since date values are not stored
        fileName =  ""
    elif dictEntry[0] == 8:
        fileName = allFilesList[2]
    else:
        fileName = allFilesList[dictEntry[0]]
    return fileName

def intToEntry(fileName, intChoice):
    fileList = ftl(fileName)
    choice = intChoice
    return fileList[choice]


#           *************************************************************************************************************************

#                                                                            DICTIONARY AND MESSAGE BODY

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



#           *************************************************************************************************************************

#                                                                            MAIN

#           *************************************************************************************************************************

root = tk.Tk()
app = fugenMain(root)
root.mainloop()


pp.copy(fullEmail)