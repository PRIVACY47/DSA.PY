# 0 1 1 2 3 5  
def fib(n):
    assert n>=0 and int(n) ==n , "oops there is an error"
    if n in [0]:
        print(n)
        return 0 

    elif n in [1]:
        print(n)
        return 1        
    else:
        v=fib(n-1)+fib(n-2)
        print(v)

fib(5)