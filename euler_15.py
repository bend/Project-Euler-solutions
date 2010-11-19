 
def pascal(n):
    if n == 1:
        return [ [1] ]
    else:
        result = pascal(n-1)
        lastRow = result[-1]
        result.append( [ (a+b) for a,b in zip([0]+lastRow, lastRow+[0]) ] )
        return result
#le resulat se trouvera a la ligne 2n et a la col 
print pascal(41)[40][20]