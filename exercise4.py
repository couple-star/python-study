lists=['jack','rose','celine']

def test(s): 
    if s in lists:
        return lists.index(s)+1
    else:
        lists.append(s)
        return len(lists)

if __name__ == '__main__':
    while True:
        s=raw_input('please input your name,input q to exit: ')
        if s=='q':
            break
        else:
            index=test(s)
            print 'your No. is {}'.format(index)
    print 'the total list for today class is: {}'.format(lists)