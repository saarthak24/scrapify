from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")
#https://gomovies.sc/tv/game-of-thrones-season-1-free-full-watch-online/watching/?ep=65&sv=8

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

epFrames = soup.find("div", {"id": "list-eps"})

#print(epFrames)

accessToken = soup.find("a", {"title": "Episode 10: Fire and Blood"}).get("data-drive")

accessToken = "https://play.gomovies.sc/8/" + accessToken

print(accessToken)
