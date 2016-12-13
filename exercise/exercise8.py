#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 扑克牌是一种非常大众化的游戏，在计算机中有很多与扑克牌有关的游戏。
# 例如，在Windows操作系统下自带的纸牌、红心大战等。在扑克牌类的游戏中，往往都需要执行洗牌操作，就是将一副牌完全打乱，使其排列没有规律。
#
# 请编程实现发扑克牌。
# 提示： 使用random库，具体请help查看或者网上查看使用方法

import random
    
list=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
colorlist=[' hongtao',' hongfang',' heitao',' heicao']
cardlist=[]
for i in range(13):
    for j in range(4):
        card=list[i]+colorlist[j]
        cardlist.append(card)
print cardlist

random.shuffle(cardlist)

for m in range(52):
    print cardlist[m]