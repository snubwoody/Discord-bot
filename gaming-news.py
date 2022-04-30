import requests
from bs4 import BeautifulSoup

#function to get the raw html of a website
def get(url):
    
    #requests the url
    page = requests.get(url)
    #returns the page content as html
    global scraper
    scraper = BeautifulSoup(page.content, 'html.parser')
    
    
    
get("https://za.ign.com/article/news?keyword__type=game")



def parse():
    #gets all the divs with m as thier class name
    val = scraper.find_all("div","m")
    head = []
    p = []
    links = []
    #gets the specified elements and puts them in arrays
    for a in val:
        head.append(a.h3.text)
        p.append(a.p.text)
        links.append(a.h3.a['href'])
    
    
parse()
    



