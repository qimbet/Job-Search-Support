#This script helps the creation of cover letters. 

#Roughly 300-500 words total for a cover letter
#Be concise. Balance enthusiasm and professionalism.

import pdfkit
import sqlite3

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
            
            PRIMARY KEY(identifier))""")

conn.commit()   #use this line whenever the table is updated

#----------------------------------------------------------------------------------------------
#
#           FUNCTION DEFINITIONS
#
#----------------------------------------------------------------------------------------------

def lookup(table, searchText):  #returns the primary key associated with the searchText value
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
    
def add(table, valuesToAdd, valuesCategories):
    numVals =  len(valuesToAdd)
    qMarkBitstring = "?,"
    qMarks = ""

    for elements in numVals:
        qMarks += qMarkBitstring
    qMarks = qMarks[:-1] #removes the last character (i.e. the trailing comma)
    
    cursor.execute(f"""
        INSERT INTO wardenRecords (identifier, originalFileLocation, originalFileName, releaseDate)
        VALUES {qMarks} 
    """,(identifier, originalFileDirectory, fileName, calculateRelease(jailTimeWeeks),)) 
    
    cursor.execute(command, (searchText,))

#----------------------------------------------------------------------------------------------
#
#           TEXT VARIABLES
#
#----------------------------------------------------------------------------------------------

name = "Jacob Mattie"
email = "jacob.c.mattie@gmail.com"
phone = "778-710-7554"
region = "Burnaby, BC"

companyName = "Placeholder Company Inc."
companyAddress = ""
companyPhone = ""
hiringManager = "Hiring Manager(s)"

industry = "healthcare"
personalCommitment = "improving patient outcomes"

role = "Data Analyst"
leadSource = ""


# cursor.execute(f"""INSERT INTO text_storage (identifier, text_content) 
#                VALUES ({}, 'Sample text 1');
# """)


#----------------------------------------------------------------------------------------------
#
#           F-STRINGS
#
#----------------------------------------------------------------------------------------------

#Lookup keys: 
#companyName --> address, phone, hiringManager
#industry --> personalCommitment

personalInfo = f"""{region} | {email} | {phone}"""
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

introduction.replace("\n", " ")
para1.replace("\n", " ")
para2.replace("\n", " ")
para3.replace("\n", " ")

#----------------------------------------------------------------------------------------------
#
#          CSS FORMATTING
#
#----------------------------------------------------------------------------------------------

font = "Roboto"
accentColour = "#00786c"


cssPortion = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jacob Mattie - Cover Letter - {role}</title>
    <style>

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
            <p>{personalInfo}</p>
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

path_to_wkhtmltopdf = "C:\Program Files\wkhtmltopdf\bin" 
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Example of generating a PDF
pdfkit.from_string(cssPortion + HTMLPortion, f"{name} - Cover Letter for {companyName} - {role}.pdf", configuration=config)