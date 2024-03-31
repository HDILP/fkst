# coding: UTF-8

import requests
import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url = "https://api.yaerxing.com/GetDiscoverTagNotes2"
headers = {
    "Accept": "application/json",
    "User-Agent": "android",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "380",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

params = {
    'device': 'R9',
    'unionid': 'otJFa09hMXKizNDdufEyjjTEKkAw',
    'height': '1920',
    'appid': 'wx2bd42ba7f4c547f5',
    'app_v': '1.13.10',
    'timestamp': "1711865527",
    'api_sig': 'ADBF11104E769E011F6A5194075580DB',
    'api_key': 'a77190573ddc0f1586bd2ef0497e2733',
    'os_v': '23',
    'rom': 'OPPO',
    'platform_id': '2',
    'flag': '1004',
    'openid': 'okvxLv2YTrsRnrp7JdtAZXtdzi60',
    'call_id': '1711865527984',
    'brand': 'OPPO',
    'width': '1080',
    'device_token': '',
    'page': '0',
    'type': '10',
    'channel': 'none',
    'model': 'OPPO R9m'
}

# 发送POST请求
response = requests.post(url, headers=headers, data=params)

if response.status_code == 200:
    print("ok:", response.json())
else:
    print("fuck:", response.status_code)
