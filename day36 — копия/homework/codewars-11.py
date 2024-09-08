def kebabize(string):
    kebab_case = []
    for i, char in enumerate(string):
        if char.isupper():
            if i != 0:
                kebab_case.append('-')
            kebab_case.append(char.lower())
        elif char.isalpha():  
            kebab_case.append(char)
    
    return ''.join(kebab_case)


print(kebabize("camelsHaveThreeHumps"))  
print(kebabize("camelsHave3Humps"))      
print(kebabize("CAMEL"))                 