#marche mais met plusieurs heures...
def fibo():
    fn1=1  #fn-1
    fn2=1  #fn-2
    fn=0
    n=2
    while True:
        fn=fn1+fn2
        fn2,fn1=fn1,fn
        n+=1
        if isPandigital(fn):
            return n



def isPandigital(n):
    st = str(n)
    cmp=['1','2','3','4','5','6','7','8','9']
    begin = sorted(st[:9])
    end = sorted(st[-9:])
    return cmp==end and cmp==begin
    
print fibo()

