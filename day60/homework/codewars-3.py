def find_missing_letter(s):
    
    letters_set = set(s)
    
    
    start_char = s[0]
    end_char = s[-1]
    
    
    expected_set = set(chr(i) for i in range(ord(start_char), ord(end_char) + 1))
    
    
    missing_letter = expected_set - letters_set
    
    
    return missing_letter.pop()
