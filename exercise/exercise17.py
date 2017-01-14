#Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.



m=input('please input one number: ')

a=[]
b=''
mbin=bin(m)

for i in range(2,len(mbin)):
    a+=mbin[i]

for i in range(len(a)):
    if a[i]=='1':
        a[i]='0'
    else:
        a[i]='1'

for i in range(len(a)):
    b+=a[i]

b=int(b,2)
print b

#accept