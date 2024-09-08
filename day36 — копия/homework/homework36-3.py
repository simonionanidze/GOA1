def manual_count(collection, to_count):
    count = 0
    for item in collection:
        if item == to_count:
            count += 1
    return count


print(manual_count([1, 2, 3, 4, 2, 5], 2))           
print(manual_count(["apple", "banana", "apple"], "apple"))  
print(manual_count(["hello", "world", "hello"], "goodbye"))  
