def sum_two_smallest_numbers(numbers):
   
    positive_numbers = [num for num in numbers if num > 0]
    
    
    positive_numbers.sort()
    
    
    return positive_numbers[0] + positive_numbers[1]
