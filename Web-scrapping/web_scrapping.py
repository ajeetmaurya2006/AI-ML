import requests
from bs4 import BeautifulSoup

# Action Movies and TV Shows on IMDB
URL = 'https://www.imdb.com/search/title/?genres=action&explore=title_type,genres&view=advanced'

list_of_title_names = []
list_of_genres = []
list_of_certificates = []
list_of_year = []

data = requests.get(URL)
soup = BeautifulSoup(data.content, 'html.parser')

# //div[@class="lister-list"]/div total 50 on the first page
movies_list = soup.find('div', {'class': 'lister-list'})
# get all lists on the page
# (//div[@class="lister-list"]//h3)[1]

##################### getting titles  #########################
title_headers = movies_list.find_all('h3')
for header in title_headers:
    title_links = header.find_all('a')
    for link in title_links:
        list_of_title_names.append(link.text)
##################### getting year of make  #########################
    years = header.find_all('span')
    # list_of_year.append(years[1].text[1: 5]) # commenting the cleaning step. This will be performed with pandas
    # during data cleaning step later
    list_of_year.append(years[1].text)
################### getting genres ######################
genres = movies_list.find_all('span', {'class': 'genre'})
for g in genres:
    # list_of_genres.append(g.text.strip()) # commenting the cleaning step. This will be performed with pandas
    list_of_genres.append(g.text)
################### getting certificates ######################

certs = movies_list.find_all('span', {'class': 'certificate'})
for c in certs:
    # list_of_certificates.append(c.text.strip()) # commenting the cleaning step. This will be performed with pandas
    list_of_certificates.append(c.text)

####################### validate ######################
print(list_of_title_names)
print(list_of_genres)
print(list_of_certificates)
print(list_of_year)
