def is_pangram(sentence):
    
    sentence = sentence.lower()
    
    
    letters_found = set()
    
    
    for char in sentence:
        if 'a' <= char <= 'z':  
            letters_found.add(char)
        
        if len(letters_found) == 26:
            return True
    
    
    return len(letters_found) == 26


print(is_pangram("The quick brown fox jumps over the lazy dog"))  
print(is_pangram("The quick brown fox jumps"))  
print(is_pangram("Pack my box with five dozen liquor jugs"))  