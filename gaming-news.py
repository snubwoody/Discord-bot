import requests
from bs4 import BeautifulSoup


url = "https://gameranx.com/news/"

page = requests.get(url)



scraper = BeautifulSoup(page.content, 'html.parser')

print(scraper)



