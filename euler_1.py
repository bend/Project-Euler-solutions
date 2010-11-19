 N     = 200
 liste  = range(2, N)                           # liste de 2 à N
 nombre = 2
 while nombre*nombre <= N:                      # tant que le nb premier < a la
                                                # racine carree de N
    for i in liste[ liste.index(nombre) + 1: ]: #parcourt la liste avec ce nombre
        if i % nombre == 0:                     #un multiple du nombre est trouve
            del liste[ liste.index(i) ]         # on le raye de la liste
    nombre = liste[liste.index(nombre) + 1]     # on prend le nombre suivant non raye
 
 print liste    
