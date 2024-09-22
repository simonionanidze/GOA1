def series_sum(n):
    sum = 0.0
    denominator = 1.0
    
    for i in range(n):
        sum += 1 / denominator
        denominator += 3
    
    return f"{sum:.2f}"

print(series_sum(5))  
print(series_sum(0))  
print(series_sum(3))  
