import json

import requests

# 热搜接口
url = "https://www.douyin.com/aweme/v1/web/hot/search/list/"

headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "dnt": "1",
    "referer": "https://www.douyin.com/hot",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    
}

# 发送params是为了获取置顶热搜
params = {
    "aid": 6383,
    "version_code": 170400
}

def get_hot_searches():
    hot_searches = {}
    response = requests.get(url, headers=headers, params=params)
    response_json = json.loads(response.content)
    hot_searches = response_json["data"]["word_list"]
    return hot_searches