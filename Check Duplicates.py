

# check excel
import xlrd
import requests
from requests.exceptions import MissingSchema
from collections import Counter
loc = r"C:\Users\User\Desktop\Project Hackathon\Data\Animal_Information.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# excel
temp = []
for i in range(1, sheet.nrows, 2):
    temp.append(sheet.cell_value(i, 0))


print(Counter(temp))
