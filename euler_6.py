def sumOfSquare(i):
    j=0
    sum=0
    while j<=i:
        sum = sum+(j*j)
        j=j+1
    return sum

def squareOfSum(i):
    j=0
    sum=0
    while j<=i:
        sum = sum+j
        j=j+1
    return sum*sum

s1=sumOfSquare(100)
s2=squareOfSum(100)
print s2-s1

        