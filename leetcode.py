arr = [15, 14, -13, 12, -11, 10, 9, 8, 7, 6, -5, -4, -3, -2, -1]

result = []
negative_sum = 0
positive_numbers = 0
for num in arr:
    if num > 0 and num != 0:
        positive_numbers += 1
        if num < 0 and num != 0:
            negative_sum += num
    else:
        return result
return [positive_numbers, negative_sum]