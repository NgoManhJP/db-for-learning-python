import openpyxl
import os
os.chdir('E:\IT\Python\GitHub\db-for-learning-python')

workbook = openpyxl.load_workbook('example.xlsx')
# print(type(workbook))
sheet = workbook.get_sheet_by_name('Sheet1')
# print(type(sheet))
# print(workbook.get_sheet_names())

