import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

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


def parse_realitatea():

    print("executing parse")
    URL = "https://realitatea.md/toate-stirile/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,"html.parser")
    stiri = soup.find_all("div", class_="article-header")
    
    list = []
    for article in stiri:
      list.append({'titlu':"realitatea", 'brief':article.text})


    return list[0:15]

def parse_tv8():


    print("executing parse")
    URL = "https://tv8.md/"
    #page = requests.get(URL)
    
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")

    browser = webdriver.Chrome(chrome_options=opts, executable_path="chromedriver")
    browser.get(URL)
    WebDriverWait(browser, 5)
    html = browser.page_source

   # print(html)


    browser.quit()

    soup = BeautifulSoup(html,"html.parser")
    stiri = soup.find("div", attrs={"role" : "tabpanel"})
    titluri = stiri.find_all("h5")
    
    list = []
    for article in titluri:
      list.append({'titlu':"tv8", 'brief':article.text})


    return list[0:15]

def parse_pointmd():


    print("executing parse")
    URL = "https://old.point.md/ru/novosti/"
    
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")

    browser = webdriver.Chrome(chrome_options=opts, executable_path="chromedriver")
    browser.get(URL)
    WebDriverWait(browser, 5)
    html = browser.page_source

    browser.quit()

    soup = BeautifulSoup(html,"html.parser")
    stiri = soup.find_all("article")
    
    list = []
    for article in stiri:
      titlu = article.find("p")
      list.append({'titlu':"pointmd", 'brief':titlu.text})

    return list[0:9]

def parse_protv():


    print("executing parse")
    URL = "https://protv.md/ultimele-%C8%99tiri"
    
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")

    browser = webdriver.Chrome(chrome_options=opts, executable_path="chromedriver")
    browser.get(URL)
    WebDriverWait(browser, 5)
    html = browser.page_source

    browser.quit()

    soup = BeautifulSoup(html,"html.parser")
    stiri = soup.find_all("div", class_="description")
    
    list = []
    for article in stiri:
      titlu = article.find("span")
    list.append({'titlu':"protv", 'brief':titlu.text})

    return list[0:15]