#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 扑克牌是一种非常大众化的游戏，在计算机中有很多与扑克牌有关的游戏。
# 例如，在Windows操作系统下自带的纸牌、红心大战等。在扑克牌类的游戏中，往往都需要执行洗牌操作，就是将一副牌完全打乱，使其排列没有规律。
#
# 请编程实现发扑克牌。
# 提示： 使用random库，具体请help查看或者网上查看使用方法

import random

list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
colorlist = [' hongtao', ' hongfang', ' heitao', ' heicao']
cardlist = []
for i in range(13):
    for j in range(4):
        card = list[i] + colorlist[j]
        cardlist.append(card)
# print cardlist

random.shuffle(cardlist)

for m in range(52):
    print cardlist[m]

# excellent

import random

# # color_dict = {0: u'红桃', 1: u'方片', 2: u'黑桃', 3: u'草花'}
# cards = range(54)
# while len(cards) > 0:
#     card = random.choice(cards)
#     cards.remove(card)
#     if card == 52:
#         print u'小王'
#     elif card == 53:
#         print u'大王'
#     else:
#         num = card / 4 + 1
#         if num == 11: num = u'J'
#         if num == 12: num = u'Q'
#         if num == 13: num = u'K'
#         color = card % 4
#         if color == 0: color = u'红桃'
#         if color == 1: color = u'方片'
#         if color == 2: color = u'黑桃'
#         if color == 3: color = u'草花'
#         print u'{0} {1}'.format(color, num)
#         # print u'{0} {1}'.format(color_dict[color], num)
