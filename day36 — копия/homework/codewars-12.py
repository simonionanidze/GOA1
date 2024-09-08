def pig_latin(word):
    vowels = 'aeiou'
    
    if word[0].lower() in vowels:
        return word + 'way'
    
    for i, char in enumerate(word):
        if char.lower() in vowels:
            return word[i:] + word[:i] + 'ay'


print(pig_latin("pig"))     
print(pig_latin("banana"))  
print(pig_latin("happy"))   
print(pig_latin("duck"))    
print(pig_latin("eat"))     
