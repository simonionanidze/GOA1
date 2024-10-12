def find_missing_number(nums):
    n = len(nums) + 1  
    num_set = set(nums)  
    for i in range(1, n + 1):
        if i not in num_set:
            return i
