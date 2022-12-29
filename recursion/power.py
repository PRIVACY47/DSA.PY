def pow(base,exp):
    assert int(exp) == exp ,"no exponent bases accepted"
    if exp==0:
        return 1
    elif exp<0:
        exp=abs(exp)
        return 1/pow(base,exp)
    return base * pow(base,exp-1)
print(pow(-2,-1))
