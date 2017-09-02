from bs4 import BeautifulSoup

import requests
import jwplayer
import openload

url = input("Enter a website to extract the URL's from: ")
#https://gomovies.sc/tv/game-of-thrones-season-1-free-full-watch-online/watching/?ep=65&sv=8

r  = requests.get(url)

data = r.text
# print(data)
soup = BeautifulSoup(data,'html.parser')

epFrames = soup.find("div", {"id": "list-eps"})

print(epFrames)

#HARD CODED
accessToken = soup.find("a", {"title": "Episode 01: Skin in the Game"}).get("data-drive")
#

print(soup.text)
print(accessToken)
accessToken = "https://play.gomovies.sc/8/" + accessToken

#     curl 'https://play.gomovies.sc/8/THo2OWFJcEEyMzJEc3dBQUJqWWsyanhzYXN6YW50SDV2dW5MUGlOUlFDRWNJdUxsN0swZnYxYW03NTV0TGFyUGM1YW5YSFRVZFFCeTZCcys4UGVxSGtlczVLbGFxTU1LcmhmM01vUTFLR2ZNY3pFdWtLN2xZeExYbExLNWxpTWlJczE5eFVFb3RLaE5YQWM5eW5acUNqSG1OMFdqbDNOT0lJRmp3Ukt5UmV6L3h3a3ZMaTVudUg0UjNDRzZVOEZQTmFLdHYxZU40SXFMTENUY0h1bHNZWGhMMzFZODZFeWwyVUEzQnFDNU85cz0=' \
# -XGET \
# -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
# -H 'Referer: https://gomovies.sc/tv/suits-season-7-free/watching/?ep=13442&sv=8' \
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    'Referer': url,
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
print(accessToken)
html = requests.get(accessToken,headers=headers).text
print(html)
print("k")
extract_vid.download_file(html)

print("Done!")
