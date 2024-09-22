def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
print(solution(10))    
print(solution(20))    
print(solution(100))   
