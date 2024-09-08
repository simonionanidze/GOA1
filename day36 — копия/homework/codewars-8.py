def reverse_data(data):
    
    segments = [data[i:i+8] for i in range(0, len(data), 8)]
    
    
    reversed_segments = segments[::-1]
    
    
    reversed_data = [bit for segment in reversed_segments for bit in segment]
    
    return reversed_data


data = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
reversed_data = reverse_data(data)
print(reversed_data)
