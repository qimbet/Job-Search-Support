#!/usr/bin/env python3
#This is a follow-up message writer for job applications, mad-libs style. 

#Current bugs: 
#printListToScroll is one iteration ahead. printListToScroll does not clear with each call
#inst.set(mood) does not reset. Every successful step forward should include a: "if mood!=default; mood=default"
#Inputting an integer for a selection breaks the program
#Program does not loop

#Currently midway through debugging printListToScroll asynchronicity. Nudging at self.currentStep

#comment legend:
"""
#% - should be revisited
#@ - exploratory debugging
"""


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

#File Names:    ----------------------------------------------------------------------
hiringManagerFile = "Hiring_Managers"
footerFile = "Personal_Info"
identityFile = "Identity"
jobFile = "Jobs"
skillsFile = "Skills"
industriesFile = "Industries"
companiesFile = "Companies"
valuesFile = "Values"
dateFile = "Dates"

#Folder Names
archiveFolder = "Letter_Archive"
dataFolder = "Data"




workingList = ["Hiring Manager", "Dates", "Jobs", "Identity", "Skills", "Industries", "Companies", "Values", "Titles"]
#                   0               1       2          3          4           5            6           7        8


workingListHardcoded = workingList #This list is reference. Used for a 'reset' button on workingList
allFilesList = [hiringManagerFile, footerFile, jobFile, identityFile, skillsFile, industriesFile, companiesFile, valuesFile, dateFile]
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

# d(programDirectory)
os.chdir(dataDir)
# d(os.getcwd())

for element in allFilesList:
    if not os.path.exists(f"{element}.txt"):
        print(f"Created new file: {element}.txt")
        makeFile(element)

#os.chdir(programDirectory)

#           *************************************************************************************************************************

#                                                                            TKINTER CLASSES

#           *************************************************************************************************************************
class fugenMain:
    def __init__(self, rootIn):
        self.currentStep = 0
        self.emailFinal = ""

        #Colours
        self.bgColour  = "#f1eacf"
        self.errColour = "#ffad95"
        self.onColour  = "#7ef191"
        self.successColour = "#6BF77D"
        self.cheerfulYellow = '#ffe918'
        self.defaultButtonColour = "#D9D9D9"

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
            promptFrame.configure(bg=self.bgColour)

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
        self.inputField = tk.Entry(textFrame, relief="sunken", justify="center")
        self.inputField.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Text output fields 
        self.instructions = tk.StringVar()
        self.promptDisplay = tk.StringVar()
        self.promptDetails = tk.StringVar()
        #3 self.prevEntries = tk.StringVar()

        #Output field display labels
        self.instructionsCell = tk.Label(self.root, textvariable=self.instructions, relief="sunken", anchor="w", justify="left", bd=2, wraplength=400)
        self.instructionsCell.grid(row=0, column=0, columnspan=2, sticky="nwse", padx=20, pady=(30,10))

        self.promptDisplayCell = tk.Label(promptFrame, textvariable=self.promptDisplay, bg=root.cget("bg"))
        self.promptDisplayCell.grid(row=0, sticky="nsew", padx=100, pady=10)
        boldFont = font.Font(weight="bold")
        self.promptDisplayCell.config(font=boldFont)

        self.promptDetailsCell = tk.Label(promptFrame, textvariable=self.promptDetails, bg=root.cget("bg"))
        self.promptDetailsCell.grid(row=1, sticky="nsew", padx=100, pady=10)

        self.root.update_idletasks()  # Update the layout
        self.promptDisplayCell.config(wraplength=promptFrame.winfo_width() - 120) 
        self.promptDetailsCell.config(wraplength=promptFrame.winfo_width() - 120) 

        self.prevEntriesList = tk.Listbox(entriesFrame, height =5)
        self.prevEntriesList.grid(row=0, column=0, sticky="nsew")
        self.scrollbar = tk.Scrollbar(entriesFrame)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.prevEntriesList.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.prevEntriesList.yview) 


        #Sets initialization values in prompt boxes
        firstPrompt = promptDict[workingListHardcoded[self.currentStep]][2][0]
        firstDetails = listToNewlineString(promptDict[workingListHardcoded[self.currentStep]][2][1:])
        firstPrevEntries = promptDict[workingListHardcoded[self.currentStep]][1][:]
        
        self.inst("You can press 'enter' instead of clicking the button\n\nPress ctrl+space to close the program\n\nWhen the program is done, you can press ctrl+v to paste the letter directly -- it copies automatically into memory :)", self.successColour)
        self.promptDisplay.set(firstPrompt) #currentStep == 0 at program start
        self.promptDetails.set(firstDetails)
        self.printListToScroll(firstPrevEntries)
        
        #Window-state Variables
        self.pinWindow = tk.BooleanVar()

        #Button definitions
        self.infoEditButton = tk.Button(buttonFrame, text="Edit Personal Information", command=self.PIPopup, padx = 5, pady = 5)
        self.programEditButton = tk.Button(buttonFrame, text="Edit Program Settings", command=self.editSettingsPopup, padx = 5, pady = 5)
        self.setOnTopButton = tk.Checkbutton(buttonFrame, text="Fix Window on screen", command=self.changePin, padx = 5, pady = 5, variable=self.pinWindow, onvalue=True, offvalue=False)

        self.infoEditButton.pack(side="top", fill="x", pady=5) 
        self.programEditButton.pack(side="top", fill="x", pady=5) 
        self.setOnTopButton.pack(side="top", fill="x", pady=5) 

        self.nextStepButton = tk.Button(self.root, text="Next Step", command=lambda: self.saveCont(workingListHardcoded[self.currentStep]), padx = 10, pady = 15, borderwidth=5)
        self.nextStepButton.grid(row=4, rowspan=1, column=0, columnspan=3, sticky="nesw", padx=35, pady=35)
        self.root.bind("<Return>", lambda event: self.nextStepButton.invoke())
        self.root.bind("<Control-space>", self.rootQuit)
        self.root.after(100, self.setFocus())

    #Window management functions
    def rootQuit(self, event=None):
        self.root.quit()

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

    #Popups
    def PIPopup(self): #Creates an instance of personalInfoPopup as a child of root
        parentWindow = tk.Toplevel(self.root)
        personalInfoPopup(parentWindow)
        self.footer = makeFooter(footerFile)

    def editSettingsPopup(self):
        parentWindow = tk.Toplevel(self.root)
        editSettingsPopup(parentWindow)

    #Display Printing
    def inst(self, message, mood=None):   #instructions. Mood sets the background colour. Note! It does not reset it afterwards
        self.instructions.set(message)
        if mood != None:
            self.instructionsCell.config(bg=mood)

    def printListToScroll(self, lst):
        d(f"\nIn printListScroll. Current step is: {self.currentStep}")
        # d(f"Printing to scrollBox:\n{lst}")
        d(f"Printing for step {self.currentStep}, which matches dictionary key {workingListHardcoded[self.currentStep]}\n")
        self.prevEntriesList.delete(0, tk.END)
        self.inputClear()
        count = 1
        for element in lst:
            self.prevEntriesList.insert(tk.END, f"{count}\t- {element} \n")
            count += 1  
    
    def showPrompt(self, dictKey):
        prompt = promptDict[dictKey][2][0]
        d(f"in showprompt: drawing on prompt value for {prompt}")
        examples = "\n".join(promptDict[dictKey][2][1:])

        if len(dictKey) >= 4: #if a substitution list exists in the Dictionary
            examples = examples.format(*dictKey[3])

        self.promptDisplay.set(prompt)
        self.promptDetails.set(examples)

    #Input Handling
    def inputClear(self): 
        self.inputField.delete(0, tk.END)
        # if err == None:                             #Not sure if this is valid, but it's worth a try
        #     self.instructions.config(bg=self.bgColour)

    def userChoiceRead(self, dictKeyEntry): #reads input, bound-checks integers. Outputs int() for a select value, "", or str() as appropriate. Variable return type!
        #d(f"in userChoiceRead\n dictKeyEntry: {dictKeyEntry}\ndictKeyEntry type = {type(dictKeyEntry)}")

        fileName = dictkeyToFileName(dictKeyEntry)
        lstLen = len(ftl(fileName))
        userInput = self.inputField.get()
        userInput = userInput.strip()
        d(f"Reading value: '{userInput}' from userChoiceRead! This is of the type {type(userInput)}\n")

        #self.currentStep = self.currentStep + 1

        if userInput.isdigit():
            userInput = int(userInput)
            if (userInput) <= lstLen:
                # d("user input: " + userInput)
                d(f"Integer input recognized! returning string value of {userInput - 1}")
                return (userInput-1)
            else:
                self.inst("ERROR:\nThe value you entered is not within bounds! \nPlease try again.", self.errColour)
                self.inputClear()
                # d(userInput)
                return False

        elif userInput == "":
            d("User input blank!")
            return userInput 
        else: #Custom/new user entry
            fileAppend(fileName, userInput)
            return userInput

    def saveInput(self, userInput):
        global workingList
        workingList[self.currentStep] = userInput

    #Program Flow
    def saveCont(self, dictKeyEntry): #saves a valid choice into memory, steps forward in program execution. Updates prompts         
        global workingList
        self.currentStep = self.currentStep + 1
        #button command: lambda:    self.saveCont(workingListHardcoded[self.currentStep])
        #the argument passed to saveCont is a dictionary Key, indexed by currentStep
        
        if self.currentStep!=0:
            d(f"savecont - standard")
            dictKeyForPrintScroll = int((promptDict[dictKeyEntry][0])) #@-1
            dictKeyForPrintScroll = workingListHardcoded[dictKeyForPrintScroll] #steps backwards. This is a hard workaround for a silly bug
        else:
            d("savecont -- current Step == 0")
            dictKeyForPrintScroll = int((promptDict[dictKeyEntry][0]))+1
            dictKeyForPrintScroll = workingListHardcoded[dictKeyForPrintScroll]
        d(f"in SaveCont: key for dictScroll: {dictKeyForPrintScroll}")

        fileName = dictkeyToFileName(dictKeyEntry)
        choice = self.userChoiceRead(dictKeyEntry)
        self.printListToScroll(promptDict[dictKeyForPrintScroll][1][:]) #print entries from ftl(fileName) to scroll
        # d(f"printing new scrollList: for entry {dictKeyForPrintScroll}")
        d(f"current dictKey: {dictKeyEntry}")
        d(f"saveCont declares: current step: {self.currentStep}")
        d(f"current choice = {choice}")

        if choice != False: #choice comes as be TYPE=str or "". 'False' denotes an error!                        
            if type(choice)== int: #%
                choice = intToEntry(fileName, choice) #converts an integer choice into the desired string
            self.saveInput(choice)
            
            if (self.currentStep == 8):
                self.inst("Program done!\n\nYou can paste your letter into your email with ctrl+v :)\n\nPress Enter to reset the program1", self.cheerfulYellow)
                self.finalize()
                self.currentStep = 0
            else:
                # self.currentStep = self.currentStep + 1
                self.inst(f"Current step is: {self.currentStep}")
                self.showPrompt(workingListHardcoded[self.currentStep]) #@
                
            d(f"input saved -- current step updated to {self.currentStep}")
        else: #error: bad input
            self.inst(f"Something's wrong! saveCont is receiving a false value from userChoiceRead!\nValue registered: {choice}, which is of type {type(choice)}", self.errColour)
            self.saveCont(dictKeyEntry) #recursive until a valid entry is attained
            exit() #%dunno how I feel about including an exit statement here
            
        #%return choice might not be the best approach. This should be the step that stores values and increments currentStep
    
    def finalize(self):
        self.buildLetter()
        self.copyMail()
        
    def buildLetter(self):
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
        os.chdir(archiveDir)
        with open(f"Reply - {workingList[2]} - {workingList[6]}.txt", "w") as file:
            file.write(self.emailFinal)
        os.chdir(dataDir)
        workingList = workingListHardcoded

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
        
class editSettingsPopup:
    def __init__(self, root):
        self.popup = root
        self.popup.title("Edit Program Info")
        #self.popup.geometry('500x400')

        self.outputField = tk.Label(self.popup, wraplength=400, text="This could be a place where you could edit, add, and remove your previous entries. However, that's more work than I currently have capacity for, so you have to do it manually.\n\nRight click on the icon you use to open the program (or look it up using your file search), and click 'Open File Location'\nOpen the 'Data' folder. Each .txt file is the list of entries for a given prompt. Click around and explore for a bit. Add, edit, or remove lines as best fits what you use.\n\nYou can press 'enter' to close this window.")
        self.outputField.grid(row=0, column=0, columnspan=3, padx=(20, 25), pady=20)

        self.closeButton = tk.Button(self.popup, text="Continue", command=self.saveClose)
        self.closeButton.grid(row=1, column=0, columnspan=3, padx=10, pady=(15, 30))
        self.popup.bind("<Return>", self.saveClose)

    def saveClose(self, event=None):        
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

def dictkeyToFileName(inputKey): #takes a dictionary key as argument
    #d(f"in dictkeyToFileName\n dictEntry: {inputKey}\ndictEntry type = {type(inputKey)}")
    dictEntry = promptDict[inputKey]
    # d("in dictkeyToFileName")
    # d(f"input key: {inputKey}")
    # d(f"dictionary entry = {dictEntry}")
    
    # if dictEntry[0] == 1: #Since date values are not stored
    #     d("\n\nno dateFile found")
    #     fileName =  ""
    if dictEntry[0] == 8:
        fileName = allFilesList[2]
    else:
        fileName = allFilesList[dictEntry[0]]
    #d(f"returning fileName: {fileName}")
    return (fileName)

def intToEntry(fileName, intChoice):
    fileList = ftl(fileName)
    choice = intChoice
    return fileList[choice]

def listToNewlineString(lst):
    z = ""
    for element in lst:
        z = z+element+"\n"
    z = z[0:-1]
    return z

#           *************************************************************************************************************************

#                                                                            DICTIONARY AND MESSAGE BODY

#           *************************************************************************************************************************
if True:
    dates = [(dt.datetime.now() - dt.timedelta(days=10)).strftime("%B %d"), (dt.datetime.now() - dt.timedelta(days=7)).strftime("%B %d")]

    #The formatting for promptDict is a little messy. I'll break it down:
    #The dictionary associates each variable (string-named) with a list of lists:
    #   [index, [previous entries], ["prompt", *"examples"], [*substitutionsForPrompts] ]

    promptDict = {
        "Hiring Manager":   
                            [0,
                                ftl(hiringManagerFile),    
                                ["What is the hiring manager's name?", 
                                "If you don't know, leave this section blank and press enter."]     
                            ],

        "Dates":            [1,   
                                dates,                     
                                ["When did you apply?", 
                                "The dates given here are 10 and 7 days ago, for convenience. Feel free to add your own."]             
                            ],

        "Jobs":             [2,
                                ftl(jobFile),              
                                ["What's the job title?"]           
                            ],

        "Identity":         [3,
                                ftl(identityFile),         
                                ["What is your academic/professional background?", 
                                "Please include the appropriate indefinite article:", 
                                "\te.g. _a_ university student",
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