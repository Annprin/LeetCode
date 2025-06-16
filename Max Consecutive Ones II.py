def MaxConsecutive(arr):
    begin, end, inv = 0, 0, 0
    max_count = 0
    for i in arr:
        if i == 1 and inv == 0:
            begin += 1
        elif i == 1 and inv == 1:
            end += 1
        elif i == 0 and inv == 0:
            inv = 1
        else:
            count = begin + inv + end
            max_count = count if count > max_count else max_count
            begin = end
            end = 0
            inv = 0

    count = begin + inv + end
    max_count = count if count > max_count else max_count
    return max_count
    
# Test 1
print(MaxConsecutive([1,0,0,0,1]))


# Test 2
print(MaxConsecutive([1,1,0,1,1]))