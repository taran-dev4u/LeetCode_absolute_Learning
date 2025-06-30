# from collections import defaultdict

# def find_all_duplicates(nums):
#     index_map = defaultdict(list)
#     for i, num in enumerate(nums):
#         index_map[num].append(i)
    
#     result = []
#     for num, indices in index_map.items():
#         if len(indices)>1:
#             result.append([num, indices])

#     return result


# nums = [3, 2, 5, 7, 3, 4, 8, 2, 5, 3, 9]
# print(find_all_duplicates(nums))


def findDuplicates(nums):
    freq = {}
    result = []

    for num in nums:
        if num in freq:
            result.append(num)
        else:
            freq[num] = 1

    return result
