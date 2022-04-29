import requests
from bs4 import BeautifulSoup

#function to get the raw html of a website
def get(url):
    
    #requests the url
    page = requests.get(url)
    #returns the page content as html
    global scraper
    scraper = BeautifulSoup(page.content, 'html.parser')
    print(url)
    
    
get("https://za.ign.com/article/news?keyword__type=game")



def parse():
    #gets all the divs with m as thier class name
    val = scraper.find_all("div","m")
    #gets the specified elements from the html
    for a in val:
      print(a.h3.text)
      print(a.p.text)
      print(a.h3.a['href'])
    
    
    
   

parse()
    



