import string

llist = string.lowercase
ulist = string.uppercase

def encrypt(x):
    u = False
    if x in ulist:
        x = x.lower()
        u = True
    if x in llist:
        i = llist.index(x)
        i -= 21
        x = llist[i]
        if u:
            x = x.upper()
        return x
    else:
        return x


if __name__ == '__main__':
    s = raw_input('Please input a sentence: ')
    _s = ''
    for i in s:
        _s += encrypt(i)
    print _s