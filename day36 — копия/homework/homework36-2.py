def manual_replace(lst, old_elem, new_elem):
    return [new_elem if x == old_elem else x for x in lst]


print(manual_replace([1, 2, 3, 4, 2, 5], 2, "two"))  
print(manual_replace(["apple", "banana", "apple", "orange"], "apple", "cherry"))  
print(manual_replace(["hello", "world", "hello"], "world", "universe"))  
