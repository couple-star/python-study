#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现百度翻译Python SDK
# http://api.fanyi.baidu.com/api/trans/product/apidoc
# APP ID: 20161220000034328
# 密钥: 2UrZfG0h0deQ76TKSH2s
# reference lib: requests: network request
#                hashlib: generate md5
#                random: generate random int
#                json: transfer json structure to dict

import requests
import hashlib
import random
import json

q=raw_input('please input your sentence: ')
froms ='en'
to='zh'
appid='20161220000034328'
salt=random.randint(9999999,100000000)
key='2UrZfG0h0deQ76TKSH2s'
strings=appid+q+str(salt)+key
md5=hashlib.md5()
md5.update(strings)
sign = md5.hexdigest()
myurl='http://api.fanyi.baidu.com/api/trans/vip/translate'
myurl=myurl+'?appid='+appid+'&q='+q+'&from='+froms+'&to='+to+'&salt='+str(salt)+'&sign='+sign
r=requests.get(myurl)
print r.text
m=json.loads(r.text).get('trans_result')
print m[0].get('src'), m[0].get('dst')

