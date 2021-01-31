import requests
from bs4 import BeautifulSoup

# Action Movies and TV Shows on IMDB
URL = 'https://www.imdb.com/search/title/?genres=action&explore=title_type,genres&view=advanced'

data = requests.get(URL)
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())