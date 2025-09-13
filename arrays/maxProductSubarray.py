from typing import List, Tuple
def maxProductsubarray(nums: List[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1
    for n in nums:
        tmp = n*curMax
        curMax = max(n*curMax, n*curMin, n)
        curMin = min(tmp, n*curMin, n)
        res = max(curMax, res)
    return res


def max