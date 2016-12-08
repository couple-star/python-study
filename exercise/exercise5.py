# -*- coding: utf-8 -*-
x=input('please input the no.: ')
s=x
a=''
c=[]
#行数字顺向排列
for i in range(x):
    if i==0:
        for j in range(x-i):
            b=str(j+1)
            a+=b+' '
    else:
        a=''
        for j in range(x-i):
            b=str(s+x-i+1+j)
            if i%2==1:
                a=b+a
            else:
                a+=b
        s=s+2*x-2*i
    c.append(a)
#print c
#行数字混合顺序排列
for i in range(x//2):
    item=c.pop(i+1)
    c.insert(x-1-i,item)
print c

#列数字排列
s=x+1
d=[]
for i in range(x-1):
    if i==0:
        for j in range(x-1-i):
            b=str(x+j+1)
            d.append(b)
    else:
        for j in range(x-1-i):
            b=str(s+(x-i)*2+j)
            d.append(b)
        s=s+2*(x-i)
print d

#把列数字插进行数字里



    
    
    
            