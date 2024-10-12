
#Given an array of integers your solution should find the smallest integer.

#For example:

#Given [34, 15, 88, 2] your solution will return 2
#Given [34, -345, -1, 100] your solution will return -345
#.You can assume, for the purpose of this kata, that the supplied array will not be empty.]


def find_smallest_integer(arr):
    return min(arr)


arr1 = [34, 15, 88, 2]
arr2 = [34, -345, -1, 100]

print(find_smallest_integer(arr1))  
print(find_smallest_integer(arr2)) 