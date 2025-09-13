# maximum subarray

from typing import List, Tuple
def max_subarray_brute(nums:List[int]) -> int:
    best = float('-inf')
    curr = 0
    pref = [0]
    for x in nums:
        pref.append(pref[-1]+x)
    n=len(nums)
    for i in nums:
        for j in range(j, n):
            best = max(best, pref[j+1]-pref[i])
    return best

print(max_subarray_brute([-1, 3, -2, 5, 0, 6, 9, -4]))


# 2 method:

def kadane(nums:List[int]) -> int:
    curr = best = nums[0]
    for x in nums[1:]:
        curr = max(x, curr+x)
        best = max(best, curr)
    return best

def kadane_with_indices(nums:List[int])-> Tuple[int, int, int]:
    best = curr = nums[0]
    start = best_l = best_r = 0
    for i in range(1, len(nums)):
        if nums[i] > curr + nums[i]:
            curr = nums[i]
            start = i
        else:
            curr += nums[i]
        if curr > best:
            best = curr
            best_l, best_r = start, i
    return best, best_l, best_r

        

def kadane_with_indices(nums: List[int]) -> Tuple[int, int, int]:
    best  = curr = nums[0]
    start = best_l = best_r = 0
    for i in range(1, len(nums)):
        if nums[i] > curr + nums[i]:
            curr = nums[i]
            start = i
        else:
            curr += nums[i]
        if curr > best:
            best = curr
            best_l, best_r = start, i
    return best, best_l, nums[best_l], best_r, nums[best_r]

print(kadane_with_indices([-1, 3, -2, 5, 0, 6, 9, -4]))
