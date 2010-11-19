#!/usr/bin/env python
liste = range(2,21)
b=False
i=21
num=0
while b==False:
    for e in liste:
        if i %e != 0:
            b=False
            num=0
            break
        else:
            b=True
            num=i
    i=i+1
print num
        