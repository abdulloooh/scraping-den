from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
from json5 import dumps

## getting album urls
album_url = "https://dawahnigeria.com/dawahcast/"

req = Request(album_url, headers={'User-Agent': 'Mozilla/5.0'})
urlClient = urlopen(req)
html_content = urlClient.read()
urlClient.close()

page_soup = soup(html_content,"html.parser")

wrappers = page_soup.findAll("section", {"id":"block-views-ramadan-1436-block-11"})

album_links = []
for w in wrappers:
  containers = w.findAll("td",{"class":"views-field views-field-title"})
  for c in containers:
    link = c.a['href']
    album_links.append(link)

##visiting each url and fetching contents

base_url = "https://dawahnigeria.com"
album = []
i = 0
for link in album_links:
    url = base_url + link
    try:
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
        # print(dumps((newAlbum)))
        album.append(newAlbum)
        i = i+1  ##just to count how many successful
    except:
        pass

print (i)
file = open("album.json", "w")
file.write(dumps(album))
file.close()