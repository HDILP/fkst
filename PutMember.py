# coding: UTF-8

import requests


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def PutMember():
    url = "https://api.yaerxing.com/UploadCartMember"

    headers = {
        "Accept": "application/json",
        "User-Agent": "android",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "387",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }

    data = {
        'device': 'R9',
        'unionid': 'otJFa09hMXKizNDdufEyjjTEKkAw',
        'height': '1920',
        'appid': 'wx2bd42ba7f4c547f5',
        'app_v': '1.13.10',
        'timestamp': '1711867514',
        'api_sig': '5C60EFDB44FC499D73A1A48A81A0587B',
        'api_key': 'a77190573ddc0f1586bd2ef0497e2733',
        'os_v': '23',
        'rom': 'OPPO',
        'platform_id': '2',
        'openid': 'okvxLv2YTrsRnrp7JdtAZXtdzi60',
        'call_id': '1711867514189',
        'brand': 'OPPO',
        'width': '1080',
        'uid': '12804388',
        'num': '1',
        'device_token': '',
        'type': '10',
        'channel': 'none',
        'scene': '1',
        'model': 'OPPO R9m'
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=data)

    # 检查响应
    if response.status_code == 200:
        result = response.json()  # 如果API返回JSON格式数据
        print(result)
    else:
        print(f"请求失败，状态码：{response.status_code}")
