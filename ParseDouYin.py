import requests
import re


def get_video_id(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Upgrade-Insecure-Requests': '1'
    }
    data = requests.get(headers=header, url=url, timeout=5)
    video_id = re.findall(r'\d+', data.url)
    return video_id[0]


def parse(url):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_list = re.findall(pattern, url)
    url = url_list[0]

    video_id = get_video_id(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Upgrade-Insecure-Requests': '1'
    }
    response = requests.get(
        url='https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + str(video_id),
        headers=headers
    )
    response = response.json().get("item_list")[0]

    video_url = response.get("video").get("play_addr").get("url_list")[0].replace("playwm", "play")
    video_reponse = requests.get(video_url, headers=headers, allow_redirects=True)
    video_url = video_reponse.url
    print('get video url:', video_url)

    audio_url = response.get("music").get("play_url").get("url_list")[0]
    print('get audio url:', audio_url)
    
    return [video_url, audio_url]
