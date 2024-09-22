def first_non_repeating_letter(s):
    
    s_lower = s.lower()
    
    
    char_count = {}
    for char in s_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    
    for char in s:
        if char_count[char.lower()] == 1:
            return char
    
    
    return ""


print(first_non_repeating_letter("stress"))  
print(first_non_repeating_letter("moonmen")) 
print(first_non_repeating_letter("aabbcc"))  
print(first_non_repeating_letter("a"))       
