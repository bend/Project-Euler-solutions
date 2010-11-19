def power(n):
    acc=1
    for i in xrange(1, n+1):
        acc=acc*n
    return acc

def sumSquare(n):
    acc=0
    for i in xrange(1, n+1):
        acc+=power(i)
    return acc

print sumSquare(1000)          
    