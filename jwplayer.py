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
    soup = BeautifulSoup(html)
    s = soup.findAll("script",{"data-cfasync":"false"})[2].text
    t = s[s.find("sources"):s.find("}]",s.find("sources"),len(s))+2]
    print(t)

    url = t.find("\"file\":\"")
    url = t[url+8:t.find("\"",url+8,len(t))]
    print(url)
    # print(t[url+8:t.find("\"",url+8,len(t))])

    # vid_link = urllib.request.urlretrieve(url,"vid.mp4",reporthook)
    # vid_link.retrieve(url, "vid.mp4")
    print("url:",url)
    # r = requests.get(url)
    # with open("request_test.mp4", "wb") as code:
    #     code.write(r.content)
    file_name = "video.mp4"
    link = url
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                sys.stdout.flush()
    print("Download Complete!")
