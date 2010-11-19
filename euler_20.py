
def fact(n, acc):
    if n==1:
        return acc
    else:
        return fact(n-1, acc*n)
        
def sum(s):
    sum=0
    for e in s:
        sum=sum+int(e)
    return sum
i=fact(100,1)
print sum(str(i))