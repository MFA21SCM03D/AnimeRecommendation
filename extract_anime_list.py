#!usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import io

url = "https://www19.gogoanime.io/anime-list.html?page="
urls = []
session = requests.session()

content = session.get(url)
# print (content.text)

for i in range(1, 57):
	
	contents = session.get(url, params = {"page" : i})
	
	urls.append(contents)

# To store the data in the file
with io.open ("anime_list.txt", "w", encoding = "utf-8") as f:

for url in urls:

	soup = BeautifulSoup(url.text, "html.parser")

	c = soup.find_all("ul", "listing")

	for i in c : 
		
		l = i.text.strip()
		
			f.write(i.text.strip())
		

session.close()



# Pandas to create a Dataframe to store the data scrapped from the web
# Store the data into a csv file for further use

# Anime Recommendation system 
# can me implemented using the data scrapped from the web