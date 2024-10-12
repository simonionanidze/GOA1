def square_digits(num):
    
    num_str = str(num)
    
    result_str = ''
   
    for digit in num_str:
      
        result_str += str(int(digit) ** 2)
    
    return int(result_str)


print(square_digits(9119))  
print(square_digits(765))   