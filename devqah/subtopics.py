from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from json5 import dumps,loads

file = open("topics.json", "r")
topics = loads(file.read())
file.close()


## getting topics album urls with no pagination
base_url = "https://dawahnigeria.com"

i = 0

secondLevelLinkage = []  #same as midlevel

# topics = topics[0:4]

for topic in topics:
    secondLevelDict = {}
    secondLevelDict['title'] = topic['topic']
    secondLevelDict['topics'] = []
    album_url = base_url + topic['link']
    print(album_url)
    req = Request(album_url, headers={'User-Agent': 'Mozilla/5.0'})
    urlClient = urlopen(req)
    html_content = urlClient.read()
    urlClient.close()

    page_soup = soup(html_content, "html.parser")

    wrappers = page_soup.findAll("article",
                                 {"class": "node node-album node-promoted node-teaser clearfix"}) + page_soup.findAll(
        "article", {"class": "node node-album node-teaser clearfix"})
    track_wrappers = page_soup.findAll("article",
                                       {"class": "node node-track node-promoted node-teaser clearfix"}) + page_soup.findAll(
        "article", {"class": "node node-track  node-teaser clearfix"})

    for w in wrappers:
        newDict = {
            "title": w.header.a.text,
            "link": w.header.a['href'],
            "type" : "album"
        }
        secondLevelDict['topics'].append(newDict)
        i = i + 1
    for w in track_wrappers:
        newDict = {
            "title": w.header.a.text,
            "link": w.header.a['href'],
            "type": "track"
        }
        secondLevelDict['topics'].append(newDict)
        i = i + 1

    ##get all links from paginated urls

    _url = album_url+ "?page="
    try:
      lastPage = page_soup.find("li", {"class": "pager-last last"}).a['href'].split("=")
      lastPage = lastPage[len(lastPage) - 1]
    except:
      lastPage = 1

    for page_number in range(1, int(lastPage)+1):
        url = _url + str(page_number)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urlClient = urlopen(req)
        html_content = urlClient.read()
        urlClient.close()

        page_soup = soup(html_content, "html.parser")

        wrappers = page_soup.findAll("article",
                                     {"class": "node node-album node-promoted node-teaser clearfix"}) + page_soup.findAll(
            "article", {"class": "node node-album node-teaser clearfix"})
        track_wrappers = page_soup.findAll("article", {
            "class": "node node-track node-promoted node-teaser clearfix"}) + page_soup.findAll("article", {
            "class": "node node-track  node-teaser clearfix"})

        for w in wrappers:
            newDict = {
                "title": w.header.a.text,
                "link": w.header.a['href'],
                "type": "album"
            }
            secondLevelDict['topics'].append(newDict)
            i = i + 1
        for w in track_wrappers:
            newDict = {
                "title": w.header.a.text,
                "link": w.header.a['href'],
                "type": "track"
            }
            secondLevelDict['topics'].append(newDict)
            i = i + 1
    secondLevelLinkage.append(secondLevelDict)

print (i)
file = open("topics-subtopics.json", "w")
file.write(dumps(secondLevelLinkage))
file.close()


