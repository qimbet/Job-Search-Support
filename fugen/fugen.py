#!/usr/bin/env python3
#This is a follow-up message writer for job applications, mad-libs style. 


import os 
import datetime as dt
import pyperclip as pp

debug = False
def d(msg):
    if debug == True:
        print(msg)

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

d("Made directories")

programDirectory = os.path.dirname(os.path.realpath(__file__))  
archiveDir = os.path.join(programDirectory, archiveFolder)
dataDir = os.path.join(programDirectory, dataFolder)

d(programDirectory)
os.chdir(dataDir)
d("changed to dataDir")
d(os.getcwd())

for element in allFilesList:
    if not os.path.exists(f"{element}.txt"):
        print(f"Created new file: {element}.txt")
        makeFile(element)

#Functions    ----------------------------------------------------------------------

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
            fileAppend(fileName, tempList)
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

My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As a {}, I carry {} that uniquely positions me to {}.  

Drawn to {} because of your {}, I wanted to re-express my interest in joining your team. I appreciate any information you are able to provide regarding my application, and cordially state my availability for an interview.  

I have re-attached my resume for your convenience.

Looking forward to hearing from you! """
    return body

#           *************************************************************************************************************************

#                                                                            MAIN

#           *************************************************************************************************************************
#PromptFill    ----------------------------------------------------------------------

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
skillPrompt = f"As {identity}, I carry [an understanding of _________] that uniquely positions me to thrive...\n ex.\n - a highly developed understanding of [x]\n- an aptitude in [y]\n"
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