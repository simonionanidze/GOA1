import re

def sum_of_numbers(s):
    
    numbers = re.findall(r'\d+', s)
    
    return sum(int(num) for num in numbers)
