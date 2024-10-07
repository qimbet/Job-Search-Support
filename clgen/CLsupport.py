#This script helps the creation of cover letters. 

#Roughly 300-500 words total for a cover letter
#Be concise. Balance enthusiasm and professionalism.

import pdfkit
import sqlite3
import os
import textEditor as te

#----------------------------------------------------------------------------------------------
#
#           DIRECTORY MANAGEMENT
#
#----------------------------------------------------------------------------------------------
DEBUG_FLAG = 1 #Debug mode: 1 = ON, 0 = OFF

path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = path_to_wkhtmltopdf)

programDirectory = os.path.dirname(os.path.realpath(__file__))

folderName = "Cover Letter Archive"
if not os.path.exists(folderName):
    os.makedirs(folderName)

#----------------------------------------------------------------------------------------------
#
#           SQL FRAMEWORK
#
#----------------------------------------------------------------------------------------------

conn = sqlite3.connect("coverLetters.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE if NOT EXISTS CoverLetterPieces(
            identifier INT, 
            role TEXT, 
            industry TEXT, 
            commitment TEXT, 
            introduction TEXT, 
            para1 TEXT, 
            para2 TEXT,
            para3 TEXT,
            closing TEXT,
            PRIMARY KEY(identifier))""")

cursor.execute("""CREATE TABLE if NOT EXISTS CompanyData(
            identifier INT, 
            companyName TEXT,
            companyAddress TEXT, 
            companyPhone TEXT, 
            hiringManager TEXT, 
            industry TEXT,
            PRIMARY KEY(identifier))""")

cursor.execute("""CREATE TABLE if NOT EXISTS personalInfo(
            identifier INT, 
            name TEXT,
            address TEXT, 
            city TEXT,
            postal code TEXT,
            phone TEXT, 
            email TEXT,
            website TEXT,
            PRIMARY KEY(identifier))""")

conn.commit()   #use this line whenever the table is updated


#----------------------------------------------------------------------------------------------
#
#           FUNCTION DEFINITIONS
#
#----------------------------------------------------------------------------------------------

#   --- --- ---  DEBUGGING --- --- ---

def d(input):   #debug message if DEBUG_FLAG = 1
    if(DEBUG_FLAG == 1):
        print(input)

#   --- --- ---  SQL --- --- ---

def lookup(table, searchText):  #returns the primary key associated with the searchText value. Should this be updated to refine by column?
    query = f"""SELECT identifier
        FROM {table}
        WHERE text_content = ?""" 
    
    cursor.execute(query, (searchText,))
    results = cursor.fetchall()
    if (len(results) == 1):
        return int(results) #returns results in integer format
    else:
        print("Caution! Duplicate entries -- the lookup returned more than one primary key for the search")
        return int(results[0]) #returns the primary key of the first viable entry
    
def matchValues(table, key, seekList): #returns all values matching a given key, in the binary-bool list defined by seekList
    #seekList is a binary list (1 = true, 0 = false), denoting whether a given value is sought
    #e.g. companyName=False, companyAddres = True, companyPhone = False; --> [FALSE, TRUE, FALSE, ...]

    cursor.execute(f"PRAGMA table_info({table})")
        # #PRAGMA table_info returns a list of tuples, one for each column. Each tuple of the form: 
        # Column id         INT     #starts at 0
        # Column name       STR 
        # Data Type         STR
        # notNull (whether value can be null) BOOL/INT
        # Default Value     STR
        # Primary Key       BOOL/INT
    columnAllData = cursor.fetchall()
    
    count = 0
    columnNames = []
    for element in columnAllData:
        columnNames[count] = element[1] #returns the column names of the table. 
        count += 1
    
    count = 0
    returnList = []
    for element in seekList:
        if (element == 1):
            cursor.execute(f"SELECT {columnNames[count]} FROM {table} WHERE identifier = ?", (key,))
            returnValue = cursor.fetchall()
        returnList.append(returnValue)
        count += 1
    
    return returnList
    
def allRowValues(table, key): #returns all table values matching a given key
    cursor.execute(f"SELECT * from {table} where identifier = ?", (key,))
    results = cursor.fetchall()
    return results
    
def add(table, valuesToAdd, valuesCategories): #adds values to a table. Inputs must be either matched lists, or strings
    d("beginning 'add' function")
    d(f"test input: {table}")
    if (type(valuesToAdd) == list):
        d("list type ADD")
        stringToAdd = ""
        for element in valuesToAdd:
            stringToAdd += "f{element}, "
        stringToAdd = stringToAdd[:-2] #removes trailing comma, whitespace

        stringCategories = ""
        for element in valuesCategories:
            stringCategories += "f{element}, "
        stringCategories = stringCategories[:-2] #removes trailing comma, whitespace
    
        for entry in range(len(valuesToAdd)):
            SQLcommand = f"INSERT INTO {table} {stringCategories[entry]} VALUES (?)"    
            cursor.execute(SQLcommand, (stringToAdd[entry],))
    
    elif (type(valuesToAdd)==str):
        d("ADD: string")
        stringToAdd = valuesToAdd
        stringCategories = valuesCategories

        SQLcommand = f"INSERT INTO {table} {stringCategories} VALUES (?)"    
        cursor.execute(SQLcommand, (stringToAdd,))       
    
    conn.commit()


#   --- --- ---  TEXT HANDLING --- --- ---

def textEditor():
    textInputWindow = te.TextEditorInstance()
    textInputWindow.run()
    inputText = textInputWindow.current_text
    textInputWindow.cleanup()
    return inputText

def firstTimeUse():
    print("Welcome! Let's get you set up with some personal info. \nEnter these as you'd like to see them on your cover letter, or leave blank to skip.\n\n")
    dataList = ["name", "email", "phone", "city", "postal code", "website"] 

    categoryList = []
    count = 0
    for entry in dataList:
        if (entry == "postal code"): #exception
            categoryList.append("postalCode")  #since SQL tables behave oddly if they contain a space. This is somewhat clunky, but makes the code scaleable
        else:
            categoryList.append(dataList[count])
        count +=1

    count = 0
    for element in dataList:
        dataList[count] = (f"Please enter your {dataList[count]}")
        count +=1

    add("personalInfo", dataList, categoryList)

#----------------------------------------------------------------------------------------------
#
#           TEXT VARIABLES
#
#----------------------------------------------------------------------------------------------


companyName = "Placeholder Company Inc."
companyAddress = ""
companyPhone = ""
hiringManager = "Hiring Manager(s)"

#posting-specific
industry = "healthcare"
personalCommitment = "improving patient outcomes"

#floating texts
role = "Data Analyst"
leadSource = "" #where was the posting found?

#CSS formatting
font = "Roboto"
accentColour = "#00786c"


name = "Jacob Mattie"
city = "burnaby"
email = "j_mattie@live.ca"
phone = "778-710-7554"
personalData = "test"


#----------------------------------------------------------------------------------------------
#
#           COVER LETTER TEXT BLOCKS
#
#----------------------------------------------------------------------------------------------

personalData = f"""{city} | {email} | {phone}"""
# HEADER: 50-60 words
# my contact info, same for target company

companyHeader = f"""{companyName}
{companyAddress}"""

salutation = f"""Dear {hiringManager},"""
# SALUTATION: 10-20 words
# "Dear Hiring Manager" (pref by name)

introduction = f"""What if your data processes could be seamlessly automated to reveal deeper insights? 
As an experienced researcher with a strong background in coding, automation, and communication, 
I am enthusiastic about the opportunity to enhance efficiency and uncover new opportunities at {companyName}."""
# INTRODUCTION: 50-80 words
# Job name, where I saw the ad. Brief Introduction, opening comments. Be engaging.


para1 = f"""Having worked as a Test Technologist at IBC Technologies, I demonstrated an ability to communicate with shareholders, 
as I summarized test results into written reports and presentations; summarizing large collections of test data in actionable insights. 
My contributions here allowed the company to resolve issues in model design, and release competitive products to market. 
During my data-handling tasks at IBC, I accomplished several automation initiatives through Python, Excel Scripts, and MATLAB, 
reducing labour requirements for common certification processes by orders of magnitude. 
"""
# BODY PARAGRAPHS: 200-300 words
# First paragraph: Experience, skills, achievements. Examples!


para2 = f"""In my peripheral labours, I have built my skills in data gathering, synthesis, and communication. 
Starting with a greenhouse gas emissions report for Island Futures, I gathered island-wide data on emissions sources 
which was presented in a calculator format for easy distribution and use among individual island residents."""
# Second paragraph: Show interest, and how my background aligns with company goals.
#     Show confidence and research. Tailor to job posting.

para3 = f"""Motivated by the rush of data communication, I undertook the Map the System challenge with some academic colleagues. 
Researching the challenges of rural medicine practice in BC, I interviewed pharmacists and doctors in both city and rural locations. 
Compiling our results into a written report, a website, and a 15-minute oral presentation, 
I demonstrated an ability to condense multifaceted issues into a series of policy amendments which would alleviate parts of the problem. 
"""


closing = f"""My skills, interests, and career path draw me towards the field of Data Science. 
As {companyName} needs help synthesizing its collections of data, I would be happy and eager to contribute my expertise in the field. 
For any gaps in my skillset, I am always motivated and eager to learn. 

I am available at your earliest convenience for an interview, and hope to hear back from you soon. """
# CLOSING: 50-80 words
# Express interest in the position and for an interview. Thank the hiring manager for their time.
#     Be polite and proactive.

signature = f"""Best, 

{name}
{phone}
{email}
"""
# SIGNATURE: 10-20 words

#removes formatting -- linebreaks added for readability in the IDE
introduction.replace("\n", " ")
para1.replace("\n", " ")
para2.replace("\n", " ")
para3.replace("\n", " ")

#----------------------------------------------------------------------------------------------
#
#          CSS FORMATTING
#
#----------------------------------------------------------------------------------------------

cssPortion = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jacob Mattie - Cover Letter - {role}</title>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
        """ + """body {
            font-family: {font}, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 210mm;
            height: 297mm;
            margin: 0 auto;
            padding: 40px 50px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
        }
        .personalHeader {
            text-align: center;
            margin-bottom: 50px;
        }

        .personalHeader h1 {
            margin: 0;
            font-size: 24px;
            font-weight: bold;
        """ + f"""color: {accentColour};""" + """}
        .personalHeader p {
            margin: 5px 0;
            font-size: 16px;
            color: #777;
        }
        .companyHeader {
            text-align: center;
            margin-bottom: 50px;
        }

        .companyHeader h1 {
            margin: 0;
            font-size: 24px;
            font-weight: bold;
        """ + f"""color: {accentColour};""" + """
        }
        .companyHeader p {
            margin: 5px 0;
            font-size: 16px;
            color: #777;
        }
        .content {
            line-height: 1.6;
        }
        .content p {
            margin-bottom: 15px;
        }
        .content .salutation,
        .content .closing {
            margin-bottom: 30px;
        }
        .content .signature {
            margin-top: 50px;
            text-align: right;
        }
    </style>
"""

#----------------------------------------------------------------------------------------------
#
#           HTML FORMATTING
#
#----------------------------------------------------------------------------------------------

HTMLPortion = f"""</head>
<body>
    <div class="container">
        <div class="personalHeader">
            <h1>{name}</h1>
            <p>{personalData}</p>
        </div>
        <div class="companyHeader">
            <p>{companyHeader}</p>
        </div>
        <div class="content">
            <p class="date">August 1, 2024</p>
            <p class="salutation">Dear Hiring Manager,</p>
            <p class = "paragraph1">{para1}</p>
            <p class = "paragraph2">{para2}</p>
            <p class = "paragraph3">{para3}</p>
            <p class="closing"></p>
            <div class="signature">
                <p>{signature}</p>
            </div>
        </div>
    </div>
</body>
</html>"""

#----------------------------------------------------------------------------------------------
#
#           PDF GENERATION, EXPORT
#
#---------------------------------------------------------------------------------------------- 



# Example of generating a PDF
while (True):
    userChoice = input("Press Enter to begin, or Edit to enter setup mode:\n")
    if (userChoice == ""):
        break
    elif (userChoice.lower() == "edit"):
        print("\n ---------------------------------------------------------------------------\n\t\t\t\tSETUP MODE\n\n")
        while (True):
            print("""Parameters to edit are: 
                  <Enter>   - Press enter on a blank field to return to the main menu
                  1         - First-time user setup. Edit your own name, address, phone, email, etc.""")
            editChoice = input("\n\n\nWhat would you like to edit? \n")
            if (editChoice == ""):
                print("Returning to main menu.\n\n")
                break
            elif (editChoice == "1"):
                firstTimeUse()


endFileContent = cssPortion + HTMLPortion
print("Pdf prepared. generating:    ")

os.chdir(programDirectory + f"\\{folderName}")
pdfkit.from_string(endFileContent, f"{name} - Cover Letter for {companyName} - {role}.pdf", configuration=config)


#----------------------------------------------------------------------------------------------
#
#           HOUSEKEEPING
#
#---------------------------------------------------------------------------------------------- 

conn.close()
os.chdir(programDirectory)
print(f"Cover letter generated for {companyName}")