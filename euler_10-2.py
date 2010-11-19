def erast(N):
    nombre = 2
    liste, liste[1] = range(N+1), 0
        
    while nombre**2 <= N:
        liste[nombre*2 :: nombre] = [0]*len( liste[nombre*2 :: nombre] )
        nombre += 1
    return filter(None, liste)

liste = erast(2000000)
sum=0
for e in liste:
    sum=sum+e
print sum
    