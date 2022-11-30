import requests 
from bs4 import BeautifulSoup

def parse_stiri():
    print("executing parse")
    URL = "https://stiri.md/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,"html.parser")
    mainlist = soup.find(id="mainlist")
    stiri = mainlist.find_all("article")
    list = []
    for article in stiri:
      titlu = article.find("h3")
      brief = article.find("p")
      if not titlu is None and not brief is None: list.append({'titlu':titlu.text, 'brief':brief.text})
        
    return list[0:15]
    
def parse_jurnal():
    print("executing parse")
    URL = "https://www.jurnal.md/ro/page/ultima-ora"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,"html.parser")
    mainlist = soup.find(id="ultima_articles_container")
    stiri = mainlist.find_all("div", class_="business-news-content-box")
    list = []
    for article in stiri:
      titlu = article.find("h3")
      brief = article.find("p")
      if not titlu is None and not brief is None: list.append({'titlu':titlu.text, 'brief':brief.text})
        
    return list[0:15]


def parse_publica():
    print("executing parse")
    URL = "https://www.publika.md/toate-stirile"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,"html.parser")
    stiri = soup.find_all("h3", class_="entry-title")
    
    list = []
    for article in stiri:
      list.append({'titlu':"publika", 'brief':article.text})


    return list[0:15]


print(parse_publica())

