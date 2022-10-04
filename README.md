
# Project Title

Unmerge



## Technologies used

![Language](https://img.shields.io/badge/Programming%20Language-Python-green)   
![Library](https://img.shields.io/badge/Library-Pandas-orange)

![Library](https://img.shields.io/badge/Library-openpyxl-blue)

![Library](https://img.shields.io/badge/Library-xlsxwriter-yellow)

## Description

The purpose of the subsequent project is essentially to enable the creation of numerous sheets from a given single spreadsheet with a single click.
## Who can use it

Anyone whose daily responsibility is to send Excel data to various stakeholders through email or another method such as ServiceNow or JIRA, can use this.
## Deployment




Clone the project 

```GIT
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

```
OR

Download the project and run it directly using the below command through CLI
```Python
$ Python filename.py

```
## Prerequisites

1) Git has to be installed in case you wish to clone the repository and use it.
2) In case you want to use the program directly, then only Python needs to be installed in the system and below following packages
 - Panadas
- OpenPyxl
- xlrdwriter
 For installation procedure of Python and its packages, please refer internet.
 
## Sample Screenshot
![UPLOAD](https://user-images.githubusercontent.com/114949310/193858166-fe7e7e1a-012a-4aae-b75d-7c02df10ed91.JPG)

## Sample Code

To deploy this project use

```Python

---------------------------
   ###Enter file path in below from where you are fetching the master file

file = ("C:\\Users\\Demo\\Data\\masterfile.xlsx")

workbook = pd.ExcelFile(file,engine = 'openpyxl') 
worksheets = workbook.sheet_names

  ###Enter file path in below where you want to save the generated unmerged files

newFile = ("C:\\Users\\Demo\\Documents\\Data")
for ws in worksheets:

    excelWriter = pd.ExcelWriter(newFile+"FILENAME_"+ws+".xlsx",engine='xlsxwriter')

    df = pd.read_excel(file,sheet_name=ws,engine = 'openpyxl')
    df.to_excel(excelWriter, sheet_name = ws, index = False,engine = 'openpyxl')
    excelWriter.save()
----------------------------
```

## Project Leaders


- Robert Schinbeckler
-  Michael Lewis
- Nikheel Uddagiri 
- Sunil Sistala
## Author

- Ajay Gour
