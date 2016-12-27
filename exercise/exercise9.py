#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 汉诺（Hanoi）塔源自于古印度，又称为河内塔。汉诺塔是非常著名的智力趣题，在很多算法书籍和智力竞赛中都有涉及。汉诺塔问题的大意如下：
# 勃拉玛是古印度的一个开天辟地的神，其在一个宇宙中留下了三根金刚石的棒，第一根上面套着64个大小不一的圆形金片（圆盘）。
# 其中，最大的金片在最底下，其余的依次叠上去，且一个比一个小。
# 勃拉玛要求众僧将该金刚石棒中的金片逐个地移到另一根棒上，规定一次只能移动一个金片，且金片在放到棒上时，大的只能放在小的下面，
# 但是可以利用中间的一个棒作为辅助移动使用。

<<<<<<< Updated upstream

def move(a, b, c, n):
    if n == 1:
        print a, "->", c
        return
    move(a, c, b, n - 1)
    print a, "->", c
    move(b, a, c, n - 1)

while True:
    try:
        num = input('Please input a number: ')
    except:
        print 'Error! please input a number!'
    else:
        break

move('A', 'B', 'C', num)
=======
A=[1,2,3]
B=[]
C=[]

B.append(A[0])

C.append(A[1])
B.insert(1,C[0])
C.pop(0)

C.append(A[2])
C.insert(0,B[1])
C.insert(0,B[0])

print B,C
>>>>>>> Stashed changes
