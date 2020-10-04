

# check website
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup


# Temporary
# headers = 'Animal list'
# f.write(headers)

# Opening up connection, and grabbing the page
myurl = 'https://a-z-animals.com/animals/'
openurl = uReq(myurl)
page_html = openurl.read()
openurl.close()

# Grab all animals name
page_soup = soup(page_html, "html.parser")
cells = page_soup.find("div", {"class": "az-left-box az-animals-index"})

#website
temp1 = set()
for litag in cells.find_all('li'):
    temp1.add(litag.text)

# check excel
import xlrd
import requests
from requests.exceptions import MissingSchema
from collections import Counter
loc = r"C:\Users\User\Desktop\Project Hackathon\Data\Animal_Information.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#excel
temp = set()
for i in range(1, sheet.nrows, 2):
    temp.add(sheet.cell_value(i, 0))


print(list(temp1.difference(temp)))
print(len(temp1.difference(temp)))
