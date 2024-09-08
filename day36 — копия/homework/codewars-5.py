def is_anagram(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    
    return sorted_str1 == sorted_str2


print(is_anagram("foefet", "toffee"))  
print(is_anagram("Buckethead", "DeathCubeK"))  
print(is_anagram("Hello", "Olelh"))  
print(is_anagram("hello", "world"))  