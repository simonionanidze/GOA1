def find_missing_letter(chars):
    
    full_range_sum = sum(range(ord(chars[0]), ord(chars[-1]) + 1))
    
    actual_sum = sum(ord(char) for char in chars)
   
    return chr(full_range_sum - actual_sum)
