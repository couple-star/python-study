x=raw_input('please enter one number: ')
m=x.strip()
try:
    s=eval(m)
except:
    print "you type wrong"
    exit()
if type(s)!=type(1):
    print "you type non int"
    exit()
else:
    if s>0:
        print ">0"
    elif s==0:
        print "=0"
    else:
        print "<0"
