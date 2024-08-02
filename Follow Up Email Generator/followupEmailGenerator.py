#This is a follow-up message writer for job applications, mad-libs style. 
#This may later be expanded to connect to a SQL database to engage directly with the job application tracker. 
import os
import datetime
import pyperclip

programDirectory = os.path.dirname(os.path.realpath(__file__))  

def autofill(prompt, madLib):
    count = 1
    print(f"\n\n{prompt}")
    print("Choices: \n")
    for element in madLib:
        print(f"{count} - {element}\n")
        count +=1
    while (True):
        choice = input("Would you like to use a prefill?\nEnter your choice if so, or type text manually:\n")

        if choice.isdigit():
            if (int(choice)) <= len(madLib):
                output = madLib[int(choice)-1]
                return output
            else:
                continue
        else:
            return choice

dates = [(datetime.datetime.now() - datetime.timedelta(days=10)).strftime("%B %d"), (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%B %d")]
datePrompt = "\nWhen did you apply? \n"
date = autofill(datePrompt, dates).strip()

jobs = ["Data Scientist", "Data Analyst", "Software Developer"]
jobPrompt = "\nWhat's the job title?\n"
jobTitle = autofill(jobPrompt, jobs).strip()

skills = ["a highly developed understanding of data structures and analytical algorithms", "an aptitude in unifying a broad array of technical concepts", "a robust understanding of algorithm design and quantitative analysis"]
skillPrompt = "\nAs a mathematician, I carry [an understanding of _________] that uniquely positions me to thrive...\n"
skillOfMerit = autofill(skillPrompt, skills).strip()

industries = [f"thrive in the constantly evolving role of {jobTitle}", f"contribute effective insights in the role of {jobTitle}"]
industryPrompt = f"\nI carry {skillOfMerit} that uniquely positions me to [thrive in the ________ industry]\n"
jobIndustry = autofill(industryPrompt, industries).strip()

companies = []
companyPrompt = "\nWhat is the company name?\n"
companyName = autofill(companyPrompt, companies).strip()

values = ["commitment to sustainability", "commitment to technologically-driven innovation"]
valuePrompt = f"\nWhy do you want to work at this specific company?\nDrawn to {companyName} because of your [commitment to ______]\n"
companyValue = autofill(valuePrompt, values).strip()

titles = [jobs[0], jobs[1], jobs[2], "Automation Technologist"]
titlePrompt = f"\nWhat title do you want to present yourself with?\nPosting is for: {jobTitle}\n"
personalTitle = autofill(titlePrompt, titles).strip()


messageBody = f"""Hi,
   
I sent in an application on {date} for the advertised role of {jobTitle}. I wanted to ask if you have had time to review my resume and qualifications, as well as inquire into the status of the hiring process.  

My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As a mathematician, I carry {skillOfMerit} that uniquely positions me to {jobIndustry}.  

Drawn to {companyName} because of your {companyValue}, I wanted to re-express my interest in joining your team. I appreciate any information you are able to provide, and cordially state my availability for an interview.  

I have re-attached my resume for your convenience.

Looking forward to hearing from you!  

Best,    


Jacob Mattie 
{personalTitle} 
jacob@qimbet.com
778-710-7554"""

print("Current letter is: \n")
print(messageBody + "\n\n")

folderName = "Letter_Archive"
if not os.path.exists(folderName):
    os.makedirs(folderName)

os.chdir(programDirectory + f"\\{folderName}")

with open(f"Reply - {jobTitle} - {companyName}.txt", "w") as file:
    file.write(messageBody)

pyperclip.copy(messageBody)
os.chdir(programDirectory)
