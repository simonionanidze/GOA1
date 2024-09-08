def sum_array(arr):
    if not arr:  
        return 0
    total = 0
    for num in arr:
        total += num
    return total
print(sum_array([1, 5.2, 4, 0, -1]))    
print(sum_array([]))                   
print(sum_array([-2.398]))             