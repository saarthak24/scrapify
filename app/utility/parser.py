from bs4 import BeautifulSoup

import requests
# import jwplayer
from . import extract_vid


def get_vid_url(url,episode):
    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data,'html.parser')

    epFrames = soup.find("div", {"id": "list-eps"})

    #print(epFrames)

    ep = epFrames.findAll("a")

    print(ep[1].get("title"))

    for frame in ep:
        if(frame.get("title").find("Episode " + episode) > -1):
            if((frame.get("data-drive") is not None) and (frame.get("data-drive").find("THo") > -1)):
                accessToken = (frame.get("data-drive"))

    accessToken = "https://play.gomovies.sc/8/" + accessToken

    print(accessToken)

    '''
    #     curl 'https://play.gomovies.sc/8/THo2OWFJcEEyMzJEc3dBQUJqWWsyanhzYXN6YW50SDV2dW5MUGlOUlFDRWNJdUxsN0swZnYxYW03NTV0TGFyUGM1YW5YSFRVZFFCeTZCcys4UGVxSGtlczVLbGFxTU1LcmhmM01vUTFLR2ZNY3pFdWtLN2xZeExYbExLNWxpTWlJczE5eFVFb3RLaE5YQWM5eW5acUNqSG1OMFdqbDNOT0lJRmp3Ukt5UmV6L3h3a3ZMaTVudUg0UjNDRzZVOEZQTmFLdHYxZU40SXFMTENUY0h1bHNZWGhMMzFZODZFeWwyVUEzQnFDNU85cz0=' \
    # -XGET \
    # -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
    # -H 'Referer: https://gomovies.sc/tv/suits-season-7-free/watching/?ep=13442&sv=8' \
    # -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
    '''

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
        'Referer': url,
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    html = requests.get(accessToken,headers=headers).text
    print(html)

    vid_url = extract_vid.download_file(html)
    return vid_url

    print("Done!")
