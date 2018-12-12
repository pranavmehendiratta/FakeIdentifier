# JGarcia23
# Scrap images

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


web = Request('https://www.aceable.com/blog/all-51-driver-license-designs-ranked-worst-to-best', headers={'User-Agent': 'Mozilla/5.0'})
website = urlopen(web).read()

# website = urlopen(web).read()
soup = BeautifulSoup(website)

new_images = []
images = soup.findAll('img')
i =  1

for image in images:
    temp = image.get('src')
    # if temp[:9] == 'https://d':
    img_temp = temp
    # else:
    #     continue
    nametemp = image.get('alt')
    if len(nametemp) == 0:
        filename = str(i)
        i += 1
    else:
        filename = nametemp

    imgfile = open(filename + ".jpeg", 'wb')
    imgfile.write(urlopen(img_temp).read())
    imgfile.close()