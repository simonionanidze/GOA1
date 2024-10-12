def find_odd_int(arr):
    from collections import Counter
    counts = Counter(arr)
    for num, count in counts.items():
        if count % 2 != 0:
            return num
