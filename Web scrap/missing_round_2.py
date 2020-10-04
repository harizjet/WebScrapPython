
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup

missinganimal = ['Eskimo Dog', 'Bear', 'Rat', 'Crab', 'Pig', 'Mastiff', 'Hippopotamus', 'Squirrel', 'Buffalo', 'Snail',
                 'Collie', 'Ant', 'Bulldog', 'Gar', 'Fly', 'Hare', 'Snake', 'Bird', 'Elephant', 'Siberian', 'Bull Terrier', 'Fox', 'Rhinoceros']

filename = "Animal_Missing_Information_round_2.csv"
f = open(filename, 'w')

count = 0
for litag in missinganimal:
    count += 1
    print(count)
    # Opening up connection, and grabbing the page
    temp = None
    litag = litag.lower()
    try:
        temp = litag.replace(' ', '-')
        myanimalurl = f'https://a-z-animals.com/animals/{temp}/'
    except AttributeError:
        myanimalurl = f'https://a-z-animals.com/animals/{litag}/'

    try:
        openurl = uReq(myanimalurl)
        page_html = openurl.read()
        openurl.close()
    except HTTPError:
        print(litag)
        print(temp)
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
