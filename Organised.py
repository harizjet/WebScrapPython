

import xlrd

loc = r'C:\Users\User\Desktop\Project Hackathon\Data\Animal_Information.xlsx'
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

import pandas as pd

xlsx = pd.ExcelFile(
    r'C:\Users\User\Desktop\Project Hackathon\Data\Animal_Information.xlsx')
animal_df = pd.read_excel(xlsx, header=None)

filename = r'Animal_Unique.csv'
f = open(filename, 'w')

# find unique column
temp = set()
for i in range(0, len(animal_df.index), 2):
    for x in animal_df.loc[i]:
        temp.add(x)

temp = [x for x in temp if not pd.isnull(x)]

tempstr = ' '
for x in temp:
    tempstr += f'{x}, '

# write unique column as header
f.write(tempstr)
f.write('\n')

# find similar label and value pair
for i, row in animal_df.iterrows():
    if i != 0:
        if i % 2 != 0:
            continue
    for column in temp:
        Novalue = True
        for x, label in enumerate(row):
            if column == label:
                f.write(str(animal_df.iloc[i + 1][x]) + ',')
                Novalue = False
                break
        if Novalue:
            f.write(' ,')

    f.write('\n')
f.close()
