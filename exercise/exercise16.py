#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
#Given two integers x and y, calculate the Hamming distance.

n=input('please input one numbers<2^31:')
m=input('please input another number<2^31: ')


nbit=bin(n)
mbit=bin(m)

na=[]
mb=[]
count=0

print nbit, mbit

for i in nbit:
    na+=i
na.pop(0)
na.pop(0)
na_lenth=len(na)
for j in range(32-na_lenth):
    na=['0']+na
print na

for i in mbit:
    mb+=i
mb.pop(0)
mb.pop(0)
mb_lenth=len(mb)
for j in range(32-mb_lenth):
    mb=['0']+mb
print mb

for i in range (32):
    if na[i]!=mb[i]:
        count+=1
print count


##accept

