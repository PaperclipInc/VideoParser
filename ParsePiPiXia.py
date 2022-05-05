import requests
import re

def parse_pipixia(url):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_list = re.findall(pattern, url)
    url = url_list[0]

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Upgrade-Insecure-Requests': '1'
    }

    response = requests.get(url)
    origin = response.history[0]
    video_id = re.findall(r"item/(.*)\?", response.history[0].headers["Location"])[0]
    api_response = requests.get("https://is.snssdk.com/bds/cell/detail/?cell_type=1&aid=1319&app_name=super&cell_id=" + video_id)
    video_url = api_response.json()["data"]["data"]["item"]["origin_video_download"]["url_list"][0]["url"]
    return ([video_url], [])
