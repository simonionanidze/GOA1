def subtract_sum(n):
   
    digits = [int(d) for d in str(n)]
    
    digit_sum = sum(digits)
    
    computed_value = sum(10 ** d for d in digits)
    
    result = computed_value - digit_sum
    
    return result
