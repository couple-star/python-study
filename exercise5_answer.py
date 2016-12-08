def snakeNum(n):
    a = [[0 for i in range(n)] for j in range(n)]
    print a

    p = 0
    q = n - 1
    t = 1
    while p < q:
        for i in xrange(p, q):
            a[p][i] = t
            t += 1
        for i in xrange(p, q):
            a[i][q] = t
            t += 1
        for i in xrange(q, p, -1):
            a[q][i] = t
            t += 1
        for i in xrange(q, p, -1):
            a[i][p] = t
            t += 1
        p += 1
        q -= 1
    if p == q: a[p][p] = t
    # for i in range(n):
    #     print a[i]
    for i in a:
        for j in i:
            print str(j) + '\t',
        print '\n'

snakeNum(8)