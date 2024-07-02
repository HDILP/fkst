# coding: UTF-8
import requests
import sys
import io
import json
import re
import time
from datetime import datetime
# import PutMember


def SendPost():
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
    # list1_64 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    #             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
    #             55, 56, 57, 58, 59, 60, 61, 62, 63, 64]

    if response.status_code == 200:
        txt = response.json()
        # print(txt)
    else:
        print("fuck:", response.status_code)

    cart = txt["cart"]
    num = cart.keys()
    num_list = list(num)
  
    # print(num_list)
    
    # txt1 = re.findall(r'\"\d\":', txt)
    # txt2 = re.findall(r'\"\d\d\":', txt)
    # txt = txt1 + txt2
    # txt3 = []
    # for i in txt:
    #     j = re.findall(r'\"(.*?)\":', i)
    #     txt3.extend(j)
    # for i in num_list:
    #     i = int(i)
    #     list1_64.remove(i)

    # return list1_64

# 定义完整序列，注意现在是字符串形式
    complete_list_str = [str(num) for num in range(1, 65)]

    def find_missing_numbers_str(current_list):
        # 将当前列表和完整序列都转换为字符串形式进行比较
        missing_numbers = [num for num in complete_list_str if num not in current_list]
        return missing_numbers

    # 每当list1_64变化时，调用此函数
    missing = find_missing_numbers_str(num_list)
    # print(f"Missing numbers (as strings): {missing}")
    return missing


while 1:
    NonePlace = SendPost()  # 获取空白位置
    if not NonePlace:
        time.sleep(3)
    else:
        # 获取当前时间
        current_time = datetime.now()
        # 格式化并打印当前时间
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S *****')

        print("*****发现小推车空位！当前时间是:", formatted_time)
        print('空位：')
        print(NonePlace)
        time.sleep(3)

    # if 1 in NonePlace:  # 判断1号位是否空白
    #     PutMember.PutMember()  # 推
    #     print('666666666')
    #     time.sleep(86400 + 5)  # 24h + 5 second
    # else:
    #     print('fuck')
    #     time.sleep(5)
