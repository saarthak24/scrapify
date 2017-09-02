from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import sys

def reporthook(count, block_size, total_size):
    #THIS CODE IS FROM: https://blog.shichao.io/2012/10/04/progress_speed_indicator_for_urlretrieve_in_python.html
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def download_file(html):
    soup = BeautifulSoup(html,"html.parser")
    s = soup.findAll("script",{"data-cfasync":"false"})[2].text
    t = s[s.find("sources"):s.find("}]",s.find("sources"),len(s))+2]
    print(t)

    url = t.find("\"file\":\"")
    url = t[url+8:t.find("\"",url+8,len(t))]
    # print(t[url+8:t.find("\"",url+8,len(t))])

    vid_link = urllib.request.urlretrieve(url,"vid.mp4",reporthook)
    # vid_link.retrieve(url, "vid.mp4")
    # import requests
    # print("url:",url)
    # r = requests.get(url)
    # with open("request_test.mp4", "wb") as code:
    #     code.write(r.content)
    print("Download Complete!")
