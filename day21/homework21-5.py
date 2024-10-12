def descending_order(num):
    
    sorted_str = ''.join(sorted(str(num), reverse=True))
    
    return int(sorted_str)

print(descending_order(42145))      
print(descending_order(145263))     
print(descending_order(123456789))   