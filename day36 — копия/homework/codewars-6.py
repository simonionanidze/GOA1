def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


print(gcd(48, 18))  
print(gcd(1071, 462))  
print(gcd(1, 1))  