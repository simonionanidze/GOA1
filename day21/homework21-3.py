def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


print(count_vowels("hello"))  