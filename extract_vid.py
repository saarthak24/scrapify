from bs4 import BeautifulSoup

soup = BeautifulSoup(open("vid.html"))
s = soup.findAll("script",{"data-cfasync":"false"})[2].text
t = s[s.find("sources"):s.find("}]",s.find("sources"),len(s))+2]
print(t)
