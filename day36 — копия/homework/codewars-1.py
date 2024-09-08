def sum_of_arrays(arr1, arr2):
    
    sum1 = sum(arr1)
    
    
    sum2 = sum(arr2)
    
    
    total_sum = sum1 + sum2
    
    return total_sum


array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

result = sum_of_arrays(array1, array2)
print("Sum of arrays:", result)