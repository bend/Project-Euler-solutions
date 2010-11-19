
N     = 13195
liste  = range(2, N)
nombre=2
while nombre*nombre <= N:
    for i in liste[ liste.index(nombre) + 1: ]: #parcourt la liste avec ce nombre
        if i % nombre == 0:                     #un multiple du nombre est trouve
            del liste[ liste.index(i) ]         # on le raye de la liste
    nombre = liste[liste.index(nombre) + 1]     # on prend le nombre suivant non raye

max=0;
nombre=600851475143
for i in liste:
    if nombre%i==0:
        if i>max:
            max=i
print max;
