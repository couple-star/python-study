#!/usr/bin/python
# -*- coding: utf-8 -*-
# 众所周知，哥德巴赫猜想的证明是一个世界性的数学难题，至今未能完全解决。我国著名数学家陈景润为哥德巴赫猜想的证明作出过杰出的贡献。
# 所谓哥德巴赫猜想是说任何一个大于2的偶数都能表示成为两个素数之和。

# 编写程序，验证指定范围内哥德巴赫猜想的正确性，也就是近似证明哥德巴赫猜想。

x=input('请输入任何一个大于2的偶数： ')
def isPrimeNumber(n,s):
	for k in s:
		if k*k>n:
			break
		if n%k==0:
			return None
	return n
	
prime=[]
m=0
for n in range(2,x):
	res=isPrimeNumber(n,prime)
	if res:
	    prime.append(res)
print prime
a=len(prime)

for i in range(a/2+2):
	for j in range(a/2-1,a):
	    if prime[i]+prime[j]==x:
		    m+=1
		    print prime[i],prime[j]
	if m==1:
		break
		
		  
