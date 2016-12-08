lists=['pepperoni','sausage','cheese','peppers']
select = []
for i in range(2):
    if i == 0:
        x=raw_input('please give me a topping: ')
    elif i == 1:
        x=raw_input('please give me one more topping: ')
    if x in lists:
        select.append(x)
        print 'we have {}'.format(x)
    else:
        print 'sorry, we dont have {}'.format(x)
print select
