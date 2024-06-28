#This is a follow-up message writer for job applications, mad-libs style. 
#This may later be expanded to connect to a SQL database to engage directly with the job application tracker. 
import os

date = input("When did you apply? \n")
jobTitle = input("\nWhat's the job title?\n")
skillOfMerit = input("\nAs a mathematician, I carry an understanding of _________ that uniquely positions me to thrive...\n")
jobIndustry = input(f"\nI carry an understanding of {skillOfMerit} that uniquely positions me to thrive in the ________\n")
companyName = input("\nWhat is the company name?\n")
companyValue = input("\nWhy do you want to work at this specific company?\n")
personalTitle = input("\nWhat title do you want to present yourself with?\n")


messageBody = f"""Hi,
   
I sent in an application on {date} for the advertised role of {jobTitle} .  I wanted to ask if you have you had time to review my resume and qualifications, as well as inquire into the status of the hiring process.  

My combination of experience, skill, and genuine enthusiasm for the position make me a strong candidate. As a mathematician, I carry an understanding of {skillOfMerit} that uniquely positions me to thrive in the {jobIndustry}.  

Drawn to {companyName} because of your {companyValue}, I wanted to re-express my interest in joining your team.   I appreciate any information you are able to provide, and cordially state my availability for an interview.  

Looking forward to hearing from you!  

Best,    


Jacob Mattie 
{personalTitle} 
jacob@qimbet.com
778-710-7554"""

print("Current letter is: \n")
print(messageBody + "\n\n")

while(True):
    userChoice = input(f"""Are you happy with this letter?
          If so, press enter on a blank line.
          If you would like to edit, select the variable you would like to change:

           1 - date
           2 - Target job title 
           3 - Skill of merit (I carry an understanding of...)
           4 - Industry (thrive in ...)
           5 - Company Name
           6 - Company Value (drawn to {companyName} because of your...)
           7 - Personal Title (tail of email signature)
          """)
    if userChoice == "":
        break;
    elif userChoice == 1:
        date = input("When did you apply? \n")
    elif userChoice == 2:
        jobTitle = input("\nWhat's the job title?\n")
    elif userChoice == 3:
        skillOfMerit = input("\nAs a mathematician, I carry an understanding of _________ that uniquely positions me to thrive...\n")
    elif userChoice == 4:
        jobIndustry = input(f"\nI carry an understanding of {skillOfMerit} that uniquely positions me to thrive in the ________\n")
    elif userChoice == 5:
        companyName = input("\nWhat is the company name?\n")
    elif userChoice == 6:
        companyValue = input("\nWhy do you want to work at this specific company?\n")
    elif userChoice == 7:
        personalTitle = input("\nWhat title do you want to present yourself with?\n")