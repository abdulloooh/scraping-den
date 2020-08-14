from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from json5 import dumps,loads

base_url = "https://dawahnigeria.com"
i = 0
dnsbott = []  #dawah nigeria scraped based on topic tags

file = open("topics-subtopics.json", "r")  ###edit as appropriate for the location of the json file
topics = loads(file.read())
file.close()

topics = topics[5:10]  # bit by bit

def fetchAlbumLinks(url):
    global i
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urlClient = urlopen(req)
        html_content = urlClient.read()
        urlClient.close()

        page_soup = soup(html_content, "html.parser")

        container = page_soup.findAll("div", {"class": "jp-type-playlist"})[0].findAll("div", {"class": "jp-playlist"})[
            0]
        mediaContainer = container.findAll("li")

        media = []
        for link in mediaContainer:
            audioTitle = link.a.text
            audioLink = (link.a['href'])[2:]

            newAudio = {
                "title": audioTitle,
                "link": audioLink
            }
            media.append(newAudio)

            i = i + 1  ##just to count how many successful

        return media

    except:
        return None



def fetchTrackLinks(url):
    global i
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urlClient = urlopen(req)
        html_content = urlClient.read()
        urlClient.close()

        page_soup = soup(html_content, "html.parser")
        link = page_soup.source['src'][2:]
        i = i + 1  ##just to count how many successful

        return link
    except:
        return None




##visiting each url and fetching contents

for linkage in topics:
    dnsbott_child = {"title": linkage["title"] , "topics":[]}

    for link in linkage['topics']:
        dnsbott_grand_child = {"title": link['title'] , "type":link['type'], 'pageLink': link['link']}

        url = base_url + link['link']

        if link['type'] == "album":
            dnsbott_grand_child['media'] = fetchAlbumLinks(url)
        elif link['type'] == "track":
            dnsbott_grand_child['media'] = fetchTrackLinks(url)

        dnsbott_child['topics'].append(dnsbott_grand_child)
    dnsbott.append(dnsbott_child)

print(i)

file = open("dntopics.json", "w")
##I take backup after each chunky data is processes,
##copy the contet and add it to my local dntopics.json
##too long, so I will be taking it it bit by bit
file.write(dumps(dnsbott))
file.close()


