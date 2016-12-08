lists=['yujing','jack','luting','xiaohua']
def check(x):
    if x in lists:
     #   return True
        print 'yes, that student is enrolled in the class'
    else:
     #   return False
        print 'no, that student is not in the class'
print 'welcome to the student center!'
while True:
    m=raw_input('please give me the name of a student (enter "q" to quit): ')
    if m=="q":
        print 'goodbye!'
        break
    else:
        check(m)