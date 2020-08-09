from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
from json5 import dumps

base_url = "https://dawahnigeria.com/dawahcast/a"
uri = "/189250" #this can be varied

url = base_url+uri

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
urlClient = urlopen(req)
html_content = urlClient.read()
urlClient.close()

page_soup = soup(html_content,"html.parser")

albumTitle = page_soup.h1.text
# print(albumTitle)

wrappers = page_soup.findAll("div",{"class":"panel-pane pane-custom pane-3"})
author = wrappers[0].div.h1.text
# print(author)

container = page_soup.findAll("div", {"class":"jp-type-playlist"})[0].findAll("div", {"class":"jp-playlist"})[0]
mediaContainer = container.findAll("li")

media=[]
for link in mediaContainer:
    audioTitle = link.a.text
    audioLink = (link.a['href'])[2:]
    # print(audioTitle)

    newAudio = {
        "title": audioTitle,
        "link" : audioLink
    }
    media.append(newAudio)

newAlbum = {
    "title":    albumTitle,
    "author":   author,
    "media" :   media
}
# print(albumTitle)
print(dumps((newAlbum)))