
def puissance(n,p):
    sum=1
    while p>=1:
        sum=sum*n
        p=p-1
    return sum

def sum(s):
    sum=0
    for e in s:
        sum=sum+int(e)
    return sum

i=puissance(2,1000)
print i
print sum(str(i))