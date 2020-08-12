from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from json5 import dumps,loads

file = open("topics.json", "r")
topics = loads(file.read())
file.close()


##visiting each url and fetching contents

# album_links = ['/dawahcast/a/193075', '/dawahcast/a/190770']
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

        page_soup = soup(html_content, "html.parser")

        albumTitle = page_soup.h1.text
        # print(albumTitle)

        wrappers = page_soup.findAll("div", {"class": "panel-pane pane-custom pane-3"})
        author = wrappers[0].div.h1.text
        # print(author)

        container = page_soup.findAll("div", {"class": "jp-type-playlist"})[0].findAll("div", {"class": "jp-playlist"})[
            0]
        mediaContainer = container.findAll("li")

        media = []
        for link in mediaContainer:
            audioTitle = link.a.text
            audioLink = (link.a['href'])[2:]
            # print(audioTitle)

            newAudio = {
                "title": audioTitle,
                "link": audioLink
            }
            media.append(newAudio)

        newAlbum = {
            "title": albumTitle,
            "author": author,
            "type": "album",
            "media": media
        }
        # print(albumTitle)
        # print(dumps((newAlbum)))
        album.append(newAlbum)
        i = i + 1  ##just to count how many successful
    except:
        pass

for link in album_links:
    url = base_url + link
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urlClient = urlopen(req)
        html_content = urlClient.read()
        urlClient.close()

        page_soup = soup(html_content, "html.parser")

        albumTitle = page_soup.h1.text
        # print(albumTitle)

        wrappers = page_soup.findAll("div", {"class": "panel-pane pane-custom pane-3"})
        author = wrappers[0].div.h1.text
        # print(author)

        container = page_soup.findAll("div", {"class": "jp-type-playlist"})[0].findAll("div", {"class": "jp-playlist"})[
            0]
        mediaContainer = container.findAll("li")

        media = []
        for link in mediaContainer:
            audioTitle = link.a.text
            audioLink = (link.a['href'])[2:]
            # print(audioTitle)

            newAudio = {
                "title": audioTitle,
                "link": audioLink
            }
            media.append(newAudio)

        newAlbum = {
            "title": albumTitle,
            "author": author,
            "type": "track",
            "media": media
        }
        # print(albumTitle)
        # print(dumps((newAlbum)))
        album.append(newAlbum)
        i = i + 1  ##just to count how many successful
    except:
        pass

print(i)
print(album)

url = "https://dawahnigeria.com/dawahcast/l/29489"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
urlClient = urlopen(req)
html_content = urlClient.read()
urlClient.close()

page_soup = soup(html_content, "html.parser")

title = page_soup.find("h1", {'class': "title", "id": "page-title"}).text

# author = page_soup.findAll("a", {"property":"rdfs:label skos:prefLabel", "typeof":"skos:Concept"})[1].text
# ko le werk


'''