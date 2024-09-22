def getCount(inputStr):
    vowels = "aeiouAEIOU"
    count = 0
    for char in inputStr:
        if char in vowels:
            count += 1
    return count
