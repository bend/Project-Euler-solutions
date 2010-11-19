def power(a,b):             #a^b
    res=1
    for x in xrange(0,b):
        res=res*a
    return res


def generate(a, b, c, d):
    l=[]
    for i in xrange(a,b+1):
        for j in xrange(c,d+1):
                l.append(power(i,j))
    return list(set(l)) 
print len(generate(2,100, 2,100))