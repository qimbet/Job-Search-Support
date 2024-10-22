#!/usr/bin/env python3
#This is a follow-up message writer for job applications, mad-libs style. 


import os 
import datetime as dt
import pyperclip as pp
import tkinter as tk

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

allFilesList = [hiringManagerFile, footerFile, identityFile, jobFile, skillsFile, industriesFile, companiesFile, valuesFile]

#Folder Names
archiveFolder = "Letter_Archive"
dataFolder = "Data"

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

#                                                                            BACK-END FUNCTIONS

#           *************************************************************************************************************************

def autofill(prompt, fileName):
    madLib = readFileList(fileName)
    count = 1
    print(f"\n\n{prompt}")
    if len(madLib) != 0:
        print("Choices: \n")
        for element in madLib:
            print(f"{count} - {element}\n")
            count +=1
    while (True):
        choice = input("Would you like to use a prefill?\nEnter your choice if so, or type text manually:\n")
        choice = choice.strip()

        if choice.isdigit():
            if (int(choice)) <= len(madLib):
                output = madLib[int(choice)-1]
                return output
            else:
                print("Input not recognized! Please try again:\n")
                continue
        elif choice == "":
            return ""
        else:
            tempList = []
            tempList.append(choice)
            fileAppend(fileName, tempList)
            return choice

def autofillList(prompt, madLib):
    count = 1
    print(f"\n\n{prompt}")
    if len(madLib) != 0:
        print("Choices: \n")
        for element in madLib:
            print(f"{count} - {element}\n")
            count +=1
    while (True):
        choice = input("Would you like to use a prefill?\nEnter your choice if so, or type text manually:\n")
        choice = choice.strip()

        if choice.isdigit():
            if (int(choice)) <= len(madLib):
                output = madLib[int(choice)-1]
                return output
            else:
                print("Input not recognized! Please try again:\n")
                continue
        elif choice == "":
            return ""
        else:
            tempList = []
            tempList.append(choice)
            return choice

def promptInputs(lst):
    outLst = []
    for element in lst:
        x = input(f"Please enter your {element}: ")
        outLst.append(x)
    return outLst

def readFileList(fileName):
    d("In readFileList")
    with open(f'{fileName}.txt', 'r') as file:
        allLines = []
        for line in file: 
            allLines.append(line.strip())
        return allLines

def fileReadFull(fileName):
    with open(f"{fileName}.txt", "r") as file:
        content = file.read()
    return content

def fileAppend(fileName, lst):
    with open(f'{fileName}.txt', 'a') as file:
        for element in lst:
            file.write(f"{element}\n")

def clearFile(fileName):
    with open(f'{fileName}.txt', 'w') as file:
        file.write("")

def makeFooter ():

    uchoice = input("Press enter to start the follow up email process. \nType 'setup' else to change your personal info (you only have to do this on your first setup).\n")
    if uchoice != "":
        clearFile(footerFile)
        vals = promptInputs(["Name", "email", "Phone Number"])
        fileAppend(footerFile, vals)

    footerList = readFileList(footerFile)
    footer = ""
    count = 0
    for element in footerList:
        footer = footer + element +"\n"
        if count == 0: #adds a linebreak after Name
            footer = footer + "\n"
        count += 1

    return footer

def messageBody():
    body = """Hi{},
   
I sent in an application on {} for the advertised role of {}. I wanted to ask if you have had time to review my resume and qualifications, as well as inquire into the status of the hiring process.  

My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As {}, I carry {} that uniquely positions me to {}.  

Drawn to {} because of your {}, I wanted to re-express my interest in joining your team. I appreciate any information you are able to provide regarding my application, and cordially state my availability for an interview.  

I have re-attached my resume for your convenience.

Looking forward to hearing from you! """
    return body

#           *************************************************************************************************************************

#                                                                            GUI SETUP

#           *************************************************************************************************************************
root = tk.Tk()
root.title("Follow-up Generator")
root.geometry('800x600')
root.minsize(200, 40)
root.configure(bg="#f1eacf")

#Grid Setup
root.grid_columnconfigure(0, weight=1)              
root.grid_columnconfigure(1, weight=1)              
root.grid_columnconfigure(2, weight=1)              
root.grid_rowconfigure(0, weight=1)                 #Personal Info
root.grid_rowconfigure(1, weight=1)                 #Program Info
root.grid_rowconfigure(2, weight=0)                 #Prompt Display
root.grid_rowconfigure(3, weight=1)                 #Prompt Details
root.grid_rowconfigure(4, weight=0)                 #Previous Entries
root.grid_rowconfigure(5, weight=0, minsize=150)    #text entry 
root.grid_rowconfigure(6, weight=0, minsize=150)    #step button

# Create a text input field
inputField = tk.Entry(root, relief="sunken", justify="center")
inputField.grid(row=5, column=0, columnspan=3, sticky="nesw", padx=20, pady=(15,10))

if debug==True:
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
programEditButton = tk.Button(root, text="Edit Program Settings", command=editProgramInfo, padx = 5, pady = 5)
nextStepButton = tk.Button(root, text="Next Step", command=nextStep, padx = 10, pady = 15, borderwidth=5)

infoEditButton.grid(row=0, column=2, sticky="ne", padx=10, pady=10)     
programEditButton.grid(row=1, column=2, sticky="ne", padx=10, pady=10)
nextStepButton.grid(row=6, rowspan=1, column=0, columnspan=3, sticky="nesw", padx=35, pady=35)


#           *************************************************************************************************************************

#                                                                            MAIN

#           *************************************************************************************************************************

root.mainloop()

footer = makeFooter()
d("Footer made!")
d(footer)


HMPrompt = "What is the hiring manager's name?\nIf you don't know, leave blank and press enter."
hiringManager = autofill(HMPrompt, hiringManagerFile).title()
if hiringManager != "":
    hiringManager = " " + hiringManager

dates = [(dt.datetime.now() - dt.timedelta(days=10)).strftime("%B %d"), (dt.datetime.now() - dt.timedelta(days=7)).strftime("%B %d")]
datePrompt = "When did you apply? \n"
date = autofillList(datePrompt, dates)

jobs = readFileList(jobFile)
jobPrompt = "What's the job title?\n"
jobTitle = autofill(jobPrompt, jobFile).title()

identityPrompt = "What is your academic/professional background? \nPlease include the appropriate indefinite article (i.e. 'a university student', or 'an engaged member of my community')"
identity = autofill(identityPrompt, identityFile).lower()

skills = readFileList(skillsFile)
skillPrompt = f"As {identity}, I carry [an understanding of _________] that uniquely positions me to thrive...\n ex.\n - a highly developed understanding of [x]\n - an aptitude in [y]\n"
skillOfMerit = autofill(skillPrompt, skillsFile)

industries = readFileList(industriesFile)
industryPrompt = f"I carry {skillOfMerit} that uniquely positions me to [thrive in the ________ industry]\n ex.\n - contribute value in the role of {jobTitle}\n - thrive in the constantly evolving role of {jobTitle}"
jobIndustry = autofill(industryPrompt, industriesFile)

companies = readFileList(companiesFile)
companyPrompt = "What is the company name?\n"
companyName = autofill(companyPrompt, companiesFile)

values = readFileList(valuesFile)
valuePrompt = f"Why do you want to work at this specific company?\nDrawn to {companyName} because of your [commitment to ______]\n ex.\n - commitment to sustainability\n - demonstrated support of social equity programs "
companyValue = autofill(valuePrompt, valuesFile)

titles = readFileList("Jobs")
titlePrompt = f"What title do you want to present yourself with?\nPosting is for: {jobTitle}\n"
personalTitle = autofill(titlePrompt, jobFile)

emailBody = messageBody()
bodyFormatted = emailBody.format(hiringManager, date, jobTitle, identity, skillOfMerit, jobIndustry, companyName, companyValue)
fullEmail = bodyFormatted + "\n\n" + footer

print("Current letter is: \n")
print(fullEmail + "\n\n")

os.chdir(programDirectory)
os.chdir(archiveFolder)
with open(f"Reply - {jobTitle} - {companyName}.txt", "w") as file:
    file.write(fullEmail)

os.chdir(programDirectory)
pp.copy(fullEmail)