def collatzProblem2(n,acc):
    if n==1:
        return acc+1
    elif n%2==0:
        return collatzProblem2(n/2,acc+1)
    else:
        return collatzProblem2((3*n)+1, acc+1)

def collatzProblem(n,acc):
    if n==1:
        return acc+str(n)
    elif n%2==0:
        return collatzProblem(n/2,acc+str(n))
    else:
        return collatzProblem((3*n)+1, acc+str(n))
        
def maxSeq(n):
    max=0
    number=0
    i=1
    while i<n:
        temp = collatzProblem2(i,0)
        if temp>max:
            max=temp
            number=i
        i=i+1
    return number

print maxSeq(1000000)