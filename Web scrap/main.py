

from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup

filename = "Animal_Information.csv"
f = open(filename, 'w')

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
count = 0
for litag in cells.find_all('li'):
    count += 1
    print(count)
    # Opening up connection, and grabbing the page
    try:
        temp = litag.text.replace(' ', '-')
        myanimalurl = f'https://a-z-animals.com/animals/{temp.lower()}/'
    except AttributeError:
        myanimalurl = f'https://a-z-animals.com/animals/{litag.text.lower()}/'

    try:
        openurl = uReq(myanimalurl)
        page_html = openurl.read()
        openurl.close()
    except HTTPError:
        continue

    # Grab all the properties
    page_soup = soup(page_html, "html.parser")
    cells = page_soup.find("section", {"class": "az-right-box"})

    # label animal name and animal image link
    f.write('Animal Name ,')
    f.write('Image Link ,')
    # label properties
    try:
        for property in cells.find_all('tr'):
            try:
                if property.find_all('td')[1].text:
                    try:
                        f.write(property.find_all('a')[
                                0].text.replace(',', '|') + ',')
                    except AttributeError:
                        f.write(property.find_all('a')[0].text.text + ',')
            except IndexError:
                continue
    except AttributeError:
        pass
    f.write('\n')

    # value animal name and animal image link
    try:
        f.write(page_soup.find_all('header')[1].find('h1').text + ',')
        imagetemp = page_soup.find(
            'div', {'class': 'content'}).find('img', src=True)['src']
        f.write(f'https://a-z-animals.com{imagetemp} ,')
    except TypeError:
        f.write('  ,')

    # value properties
    try:
        for property in cells.find_all('tr'):
            try:
                if property.find_all('td')[1].text:
                    try:
                        f.write(property.find_all('td')[
                                1].text.replace(',', '|') + ',')
                    except AttributeError:
                        f.write(property.find_all('td')[1].text + ',')
            except IndexError:
                continue
    except AttributeError:
        pass
    f.write('\n')

f.close()
