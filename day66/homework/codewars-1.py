def find_missing_letter(chars):
    
    ascii_values = [ord(c) for c in chars]
    
    
    min_value = min(ascii_values)
    max_value = max(ascii_values)
    
    
    full_set = set(range(min_value, max_value + 1))
    
    
    missing_value = list(full_set - set(ascii_values))[0]
    
    
    return chr(missing_value)
