def largest_five_digit_number(num):
    num_str = str(num)
    max_num = 0
    
    for i in range(len(num_str) - 4):
        for j in range(i + 5, len(num_str) + 1):
            current_num = int(num_str[i:j])
            if len(str(current_num)) == 5:
                max_num = max(max_num, current_num)
    
    return max_num
