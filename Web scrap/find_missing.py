

from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup


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
    temp = None
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
        print(litag.text)
        print(temp)
