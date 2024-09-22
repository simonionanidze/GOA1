def descending_order(num):
   
    num_str = str(num)
    
    sorted_digits = sorted(num_str, reverse=True)
    
    sorted_num = int(''.join(sorted_digits))
   
    return str(sorted_num)
