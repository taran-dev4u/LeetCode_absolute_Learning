from typing import List, Tuple

def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1]*(len(nums))
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i]
    postfix  = 1
    for i in range(len(nums)):
        res[i] *= postfix
        postfix *= nums[i]
    return res
