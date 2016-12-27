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

# good

#!/usr/bin/env python
# -*- coding=utf-8 -*-
# import hashlib
# import random
#
# import requests
#
#
# class Translate:
#     def __init__(self, sentence, from_lang=None, to_lang=None):
#         self.appid = '20161220000034328'
#         self.key = '2UrZfG0h0deQ76TKSH2s'
#         self.sentence = sentence
#         self.from_lang = from_lang if from_lang == 'zh' or from_lang == 'en' else 'auto'
#         self.to_lang = to_lang if to_lang == 'zh' or to_lang == 'en' else 'auto'
#         self.salt = random.randint(1, 100000)
#
#     def query(self):
#         string = '{0}{1}{2}{3}'.format(self.appid, self.sentence, self.salt, self.key)
#         self.md5 = hashlib.md5(string).hexdigest()
#         # print self.md5
#         base_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
#         query_url = '{0}q={1}&from={2}&to={3}&appid={4}&salt={5}&sign={6}'.format(
#             base_url,
#             self.sentence,
#             self.from_lang,
#             self.to_lang,
#             self.appid,
#             self.salt,
#             self.md5
#         )
#         r = requests.get(query_url)
#         return r.json()['trans_result']
#
#
# if __name__ == '__main__':
#     q_set = '早上好\n晚上好'
#     sss = Translate(q_set)
#     r_set = sss.query()
#     for i, j in enumerate(q_set.split('\n')):
#         print j, r_set[i]['dst']
