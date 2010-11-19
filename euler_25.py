def fiboToLenght(n):
    nm1=1
    nm2=1
    pos=1
    i=2
    while len(str(pos)) <n:
        pos=nm1+nm2
        nm2,nm1=nm1,pos
        i+=1
    return i

print fiboToLenght(1000)