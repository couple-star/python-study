#!/usr/bin/env python
# -*- coding: utf-8 -*-

n=input('please input the n: ')
m=0
num=0
i=0
string=''
vornums=0

if n<=10:
    for i in range(1,n+1):
        string+=str(i)
    end=string[n-1]

else:
    while num<n:
        num+=9*10**i*(i+1)
        i+=1

    m=i  #数字在10**(m-1)-1 和10**m之间
    for j in range(m):
        vornums+=int(9*10**(j-1)*j)#前面可以通过公式算出的位数

#    print vornums

    nums=(n-vornums)//m
    numss=(n-vornums)%m

    totalnums=10**(m-1)-1+nums

    if numss!=0:
        totalnumss=totalnums+1
        stringnum = str(totalnumss)
        end=stringnum[numss-1]
    else:
        totalnumss=totalnums
        stringnum=str(totalnumss)
        end=stringnum[m-1]

#    print m
#    print nums,numss
#    print totalnums,totalnumss
print int(end)
