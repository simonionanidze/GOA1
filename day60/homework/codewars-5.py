def diff_longest_and_shortest(text):
    
    words = text.split()
    
    
    lengths = [len(word) for word in words]
    
    
    max_length = max(lengths)
    min_length = min(lengths)
    
    
    difference = max_length - min_length
    
    return difference
