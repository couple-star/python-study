#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

#Example:
#Given a = 1 and b = 2, return 3.

def getSum(a,b):
    sum = a
    icarry = b
    if sum*icarry==-1:
        sum=0
    else:
        while icarry!=0:
            tmp = sum
            sum = tmp ^ icarry
            icarry = (tmp&icarry)<<1
    return sum;

if __name__ == '__main__':
    a = input('please input a: ')
    b = input('please input b: ')
    print getSum(a,b)



