import pandas as pd
import numpy as np
import openpyxl as op
import os
import xlsxwriter

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

print("Process completed, Please visit the provided location to get the required files....")