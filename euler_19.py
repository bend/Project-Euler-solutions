day=2
res=0
for e in range(1901, 2001):
    print e
    for i in range(1,12):
        if i==1 or i==3 or i==05 or i==7 or i==8 or i==10 or i==12:
            if day%7==0:
                res+=1
            day+=3
        elif i==4 or i==6 or i==9 or i==12:
            if day%7==0:
                res+=1
            day+=2
        else:
            if e%4==0:
                if day%7==0:
                    res+=1
                day+=1
            else:
                if day%7==0:
                    res+=1
print res
                
            
        
