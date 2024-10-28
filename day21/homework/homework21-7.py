def sum_multiples_3_or_5(number):
    if number < 0:
        return 0
    else:
        return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(sum_multiples_3_or_5(10))  