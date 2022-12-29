def sod(n):
    assert n>0 and int(n) == n ,"oops"
    if(n<10):
        return n
    return n%10 + sod(n//10)

print(sod(1234))