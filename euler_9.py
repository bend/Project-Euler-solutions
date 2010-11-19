def pythagoreanTriplet(n):
    for i in xrange(1,n):
        if(500000 - 1000*i)%(1000-i)==0:
            b=i
            a=(500000 - 1000*b)/(1000-b)
            c=1000-a-b
            return a*b*c
    return 0
print pythagoreanTriplet(1000)