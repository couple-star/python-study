c=['1 2 3 4 5 6 7 8 ', '293031323334', '49505152', '6162', '64', '585756', '4443424140', '22212019181716']
d=['9', '10', '11', '12', '13', '14', '15', '23', '24', '25', '26', '27', '28', '35', '36', '37', '38', '39', '45', '46', '47', '48', '53', '54', '55', '59', '60', '63']
for j in range(8-1):
    if j%2==0:
        for i in range(8-1-j):
        c[i+1+j/2]=c[i+1+j/2]+d[i]
#    else:
#        for i in range(8-1-j):
#        c.reverse()
#        c[i+1]=d[i]+c[i+1]
print c

    
    
    