def find_it(seq):
    
    counts = {}
    
    
    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    
    for key, value in counts.items():
        if value % 2 != 0:
            return key
