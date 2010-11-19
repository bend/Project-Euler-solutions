#!/usr/bin/env python
import math
def countdivisors(position):
    i=1
    divisor=0
    for x in xrange(1, int(math.sqrt(position)+1)):
        if position%x==0:
            divisor+=2
    return divisor

def get_answers():
    a = 0
    triangle = 0
    while True:
        a += 1
        triangle += a
        if countdivisors(triangle) > 500:
            return triangle
            False

print get_answers()
    
    


