#!/usr/bin/env python
# -*- coding: utf-8 -*-

n=input('please in put n: ')
a=[]

for i in range(1,n+1):
    if i%3==0:
        if i%5!=0:
            a.append("Fizz")
        else:
            a.append("FizzBuzz")
    elif i%5==0:
        if i%3!=0:
            a.append("Buzz")
        else:
            a.append("FizzBuzz")
    else:
        a.append(str(i))
print a

#accept