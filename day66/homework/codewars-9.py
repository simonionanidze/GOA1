def square_digits(num):
    
    num_str = str(num)
    
    squared_str = ''.join(str(int(digit) ** 2) for digit in num_str)
    
    return int(squared_str)
