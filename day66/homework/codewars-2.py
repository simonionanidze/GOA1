def multiply(arr):
    
    product = 1
    
    
    has_non_zero = False
    
    
    for num in arr:
        if num != 0:
            product *= num
            has_non_zero = True
    
    return product if has_non_zero else 0
