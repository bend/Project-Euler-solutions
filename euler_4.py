def isPalyndrome(i):
    number_string = str(i)
    if i<1000:
        return False
    elif i<10000:
        return number_string[0] == number_string[3] and number_string[1] == number_string[2]
    elif i<100000:
        return number_string[0] == number_string[4] and number_string[1] == number_string[3]
    elif i<1000000:
        return number_string[0] == number_string[5] and number_string[1] == number_string[4] and number_string[2] == number_string[3]
    

liste = range(100, 1000)
biggest =0
for e in liste:
    for j in liste:
        sum=e*j
        if isPalyndrome(sum):
            if sum>biggest:
                biggest=sum
                
print biggest