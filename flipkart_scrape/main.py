from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from json5 import dumps

url = 'https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

urlClient = urlopen(url)
html_content = urlClient.read()
urlClient.close()

page_soup = soup(html_content, "html.parser")

containers = page_soup.findAll("div" , {"class":"_3O0U0u"})

#print(len(containers))

container = containers[0]
#print(containers)

name = container.div.img['alt']
#print(name)

price = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#print(price[0].text)

rating = container.findAll("div", {"class":"hGSR34"})
#print(rating[0].text)

description = container.findAll("li", {"class":"tVe95H"})
#print(description[0].text)

#full code
flipkart = []
for container in containers:
    name = container.div.img['alt']
    rating = container.findAll("div", {"class": "hGSR34"})
    description = container.findAll("li", {"class": "tVe95H"})
    price = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})

    describtionArr = []
    if description:
        for d in description:
            describtionArr.append(d.text)

    if name and price:
        item = {
            "name": name,
            "description": describtionArr,
            "price": price[0].text,
            "rating": rating[0].text if rating else None,
        }

        flipkart.append(item)

flipkartJson= dumps(flipkart)

file = open("flipkart-electronics.json" , "w")
file.write(flipkartJson)
file.close()