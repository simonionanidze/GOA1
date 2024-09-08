def expanded_form(num):
    
    num_str = str(num)
    
    expanded_parts = []
    
    
    for i, digit in enumerate(num_str):
        
        if digit != '0':
            
            place_value = 10 ** (len(num_str) - i - 1)
            expanded_parts.append(str(int(digit) * place_value))
    
    
    return ' + '.join(expanded_parts)


print(expanded_form(12))     
print(expanded_form(42))     
print(expanded_form(70304))  
