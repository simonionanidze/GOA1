def collatz(n):
    sequence = [n]  
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    
    sequence_str = '->'.join(map(str, sequence))
    
    return sequence_str


print(collatz(4))  
print(collatz(3))  
