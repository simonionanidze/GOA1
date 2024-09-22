def find_smallest_int(arr):
 
    smallest = arr[0]
    
   
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    
    return smallest

print(find_smallest_int([34, 15, 88, 2]))     
print(find_smallest_int([1, 2, 3, 4, 5]))     
print(find_smallest_int([10, 0, -10, 5]))     
print(find_smallest_int([-5, -3, -2, -1]))    
