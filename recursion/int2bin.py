def int2bin(n):
    if (n<=1):
        return str(n)

    else:
        return int2bin(n//2) + str(n%2)

print(int2bin(-4))
