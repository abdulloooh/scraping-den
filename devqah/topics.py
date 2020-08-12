from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
from json5 import dumps


## getting english album urls with no pagination
album_url = "https://dawahnigeria.com/dawahcast/sitemap"

req = Request(album_url, headers={'User-Agent': 'Mozilla/5.0'})
urlClient = urlopen(req)
html_content = urlClient.read()
urlClient.close()

page_soup = soup(html_content,"html.parser")

wrapper = page_soup.findAll("div", {"class":"site-map-box-terms site-map-box-terms-2 site-map-box"})
containers = wrapper[0].findAll("li")
topicLinks = []
i=0
for c in containers:
  newDict = {}
  newDict["topic"] = c.a.text
  newDict["link"] = c.a['href']
  topicLinks.append(newDict)
  i = i+1

print (i)
file = open("topics.json", "w")
file.write(dumps(topicLinks))
file.close()
