def gcd(a,b):
    assert int(a)==a and int(b)==b ,"oops"
    if(a%b == 0):
        return b
    else:
        return gcd(b,a%b)

print(gcd(abs(34),abs(18)))