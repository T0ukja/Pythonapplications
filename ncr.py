
def factorial(n):
      
    if n == 0:
        return 1
     
    return n * factorial(n-1)

def ncr():
    
    n=int(input("Give n 'objcts' value"))
    r=int(input("Give r 'samples' value"))
    if r > n:
        print( " n value must be bigger than r value")
        ncr()
    else:
        r_=factorial(r)
        n_=factorial(n)
        result=n_/(r_*factorial((n-r)))
        print(result)

ncr()
