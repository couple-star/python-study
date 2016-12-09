#!/usr/bin/python
# -*- coding: utf-8 -*-
# 素数（质数）指的是不能被分解的数，除了1和它本身之外就没有其他数能够整除。

# 求100以内的所有素数。

for i in range(1,100):
	m=0
	for j in range(1,i+1):
		if i%j==0:
			m+=1
	if m==2:
		print i
	

# good

#def isPrimeNumber(n, s):
#	for k in s:
#		if k * k > n: break
#		if n % k == 0: return None
#	return n
#
#prime = []
#for n in range(2, 100):
#	res = isPrimeNumber(n, prime)
#	if res: prime.append(res)
#
#print prime