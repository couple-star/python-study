#!/usr/bin/env python
# -*- coding: utf-8 -*-
#查看一个GitHub用户的repositories，取出属于他的star排名最高的repositories,打印项目名称和star数目
#API地址是https://developer.github.com/v3/

import requests
# import json

# myurl='https://api.github.com'
# myurl=myurl+'/users/JiaKunUp/repos'
# r=requests.get(myurl)
# print r.text          #打印出里面所有的项目，字符串格式
# m=json.loads(r.text)  #改成Python能识别的模式，此时为list
# lenth=len(m)          #可得知项目的数目为30个
#
# j=0
# star=0
# for i in range(lenth):
#     projects=m[i]
#     stars=projects.get('stargazers_count')
#     if stars>star:
#         star=stars
#         j=i
#     else:
#         continue
# #print star,j

# print"the most star project is: ",m[17]
# print"the star number is: ",star

# excellent

username = raw_input('Please input a username: ')

base_url = 'https://api.github.com'
query_url = '{0}/users/{1}/repos'.format(base_url, username)
r = requests.get(query_url)
result = r.json()
# repo_list = {x['name']: x['stargazers_count'] for x in result if not x['fork']}
# sort = sorted(repo_list.items(), key=lambda e: e[1], reverse=True)
# print sort[0][0], sort[0][1]


sort = sorted(result, key=lambda e: e['stargazers_count'], reverse=True)
# print sort
print sort[0]['name'], sort[0]['stargazers_count']
