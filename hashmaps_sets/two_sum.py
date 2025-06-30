def two_sum(nums, target):
    hashmap = {}
    storing = []
    for i, num in enumerate(nums):
        sec_num = target - num
        if sec_num in hashmap:
            storing.append([hashmap[sec_num], i])
        hashmap[num] = i
    return storing
nums = [2, 6, 1, 8, 9, 5, 3, 4]
print(two_sum(nums, 10))

# trying my own

# i will proceed to get three sum

