#1,1,2,3,5,8,13,21,34
#
#
# nextnum=0
# vornum1=1
# vornum2=1
#
# if n>2:
#     for i in range(n-2):
#         nextnum=vornum1+vornum2
#         vornum1=vornum2
#         vornum2=nextnum
# else:
#     nextnum=1
#
# print nextnum

def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    n = input('please input n: ')
    print fib(n)
