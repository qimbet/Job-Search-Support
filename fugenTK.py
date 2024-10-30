import os
import datetime as dt
import pyperclip as pp
import tkinter as tk
from tkinter import messagebox

# Debug flag
debug = False
def d(msg):
    if debug:
        print(msg)

# Constants for file and folder names
hiringManagerFile = "Hiring_Managers"
footerFile = "Personal_Info"
identityFile = "Identity"
jobFile = "Jobs"
skillsFile = "Skills"
industriesFile = "Industries"
companiesFile = "Companies"
valuesFile = "Values"

allFilesList = [hiringManagerFile, footerFile, identityFile, jobFile, skillsFile, industriesFile, companiesFile, valuesFile]

archiveFolder = "Letter_Archive"
dataFolder = "Data"

# Initialize Tkinter window
root = tk.Tk()
root.title("Follow-Up Message Writer")

# Tkinter widgets
input_fields = {}

# Helper Functions
def makeFile(fileName):
    with open(f"{fileName}.txt", "a") as file:
        file.write("")

def create_directories():
    if not os.path.exists(archiveFolder):
        os.makedirs(archiveFolder)
    if not os.path.exists(dataFolder):
        os.makedirs(dataFolder)

def autofill(prompt, fileName):
    madLib = readFileList(fileName)
    if len(madLib) > 0:
        messagebox.showinfo("Choices", f"\nChoices: \n\n" + "\n".join([f"{i+1}. {item}" for i, item in enumerate(madLib)]))
    # Prompt user via GUI
    input_label = tk.Label(root, text=prompt)
    input_label.pack()
    user_input = tk.Entry(root)
    user_input.pack()

    return user_input.get()

def readFileList(fileName):
    d("In readFileList")
    with open(f'{fileName}.txt', 'r') as file:
        return [line.strip() for line in file]

def fileAppend(fileName, lst):
    with open(f'{fileName}.txt', 'a') as file:
        for element in lst:
            file.write(f"{element}\n")

def makeFooter():
    uchoice = autofill("Enter your personal info or press enter to skip:", footerFile)
    if uchoice != "":
        vals = autofill("Name, email, Phone Number:", footerFile)
        fileAppend(footerFile, vals)
    
    footerList = readFileList(footerFile)
    footer = "\n".join(footerList)
    return footer

def generate_message():
    # Collect inputs
    footer = makeFooter()
    
    hiringManager = autofill("What is the hiring manager's name?", hiringManagerFile).title()
    if hiringManager != "":
        hiringManager = " " + hiringManager
    
    date = autofill("When did you apply?", "Dates")
    jobTitle = autofill("What's the job title?", jobFile).title()
    
    identity = autofill("What is your academic/professional background?", identityFile).lower()
    skillOfMerit = autofill("As " + identity + ", I carry...", skillsFile)
    jobIndustry = autofill("I carry " + skillOfMerit + " to thrive in the...", industriesFile)
    
    companyName = autofill("What is the company name?", companiesFile)
    companyValue = autofill("Why do you want to work at this specific company?", valuesFile)
    
    emailBody = f"""Hi{hiringManager},

I sent in an application on {date} for the advertised role of {jobTitle}. I wanted to ask if you have had time to review my resume and qualifications, as well as inquire into the status of the hiring process.  

My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As a {identity}, I carry {skillOfMerit} that uniquely positions me to {jobIndustry}.  

Drawn to {companyName} because of your {companyValue}, I wanted to re-express my interest in joining your team. I appreciate any information you are able to provide regarding my application, and cordially state my availability for an interview.  

I have re-attached my resume for your convenience.

Looking forward to hearing from you!"""
    
    fullEmail = emailBody + "\n\n" + footer
    
    # Show message in window
    result_window = tk.Toplevel(root)
    result_window.title("Generated Email")
    result_label = tk.Label(result_window, text=fullEmail)
    result_label.pack()

    # Copy to clipboard
    pp.copy(fullEmail)

# Button to trigger message generation
generate_button = tk.Button(root, text="Generate Message", command=generate_message)
generate_button.pack()

root.mainloop()
