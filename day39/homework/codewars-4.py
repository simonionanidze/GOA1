import math

def century(year):
    return math.ceil(year / 100)
print(century(1705))  
print(century(1900))   
print(century(1601))   
print(century(2000))   
print(century(2001))   