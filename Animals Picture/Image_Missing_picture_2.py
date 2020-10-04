

import xlrd
import requests
from requests.exceptions import MissingSchema

loc = r"C:\Users\User\Desktop\Project Hackathon\Data\Animals Picture\Animal_Missing_Information_picture_2.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
count = 0
for i in range(1, sheet.nrows, 2):
    count += 1
    print(count)

    animal_name = sheet.cell_value(i, 0)
    image_link = sheet.cell_value(i, 1)

    # create image file
    animal_name = animal_name.replace(' ', '_').lower()
    file = open(f'{animal_name}.jpg', 'wb')

    # create image instance
    print(image_link)
    try:
        response = requests.get(image_link.strip())
    except MissingSchema:
        response = requests.get(
            'https://image.shutterstock.com/image-vector/no-user-profile-picture-hand-260nw-99335579.jpg')
    file.write(response.content)

    file.close()
