def manual_reverse(collection):
    if isinstance(collection, list):
        return collection[::-1]
    elif isinstance(collection, tuple):
        return tuple(reversed(collection))
    elif isinstance(collection, str):
        return collection[::-1]
    elif isinstance(collection, set):
        return set(reversed(collection))
    else:
        raise TypeError("Unsupported collection type")


print(manual_reverse([1, 2, 3, 4, 5]))        
print(manual_reverse((1, 2, 3, 4, 5)))       
print(manual_reverse("hello"))                
print(manual_reverse({1, 2, 3, 4, 5}))       
