#对向量a和b进行求和
# def python(n):
#     a=[]
#     b=[]
#     c=[]
#     for i in range(1,n+1):
#         a.append((i-1)**2)
#         b.append((i-1)**3)
#
#     c.append(a+b)
#     return c
#
# if __name__=='__main__':
#      print python(3)

import numpy

def numpysum(n):
    a=numpy.arange(n)**2
    b=numpy.arange(n)**3
    c=a+b
    return c

if __name__=='__main__':
     print numpysum(3)