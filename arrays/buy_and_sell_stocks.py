from typing import List, Tuple
def buy_and_sell_stocks(nums: List[int]) -> int:
    l, r = 0, 1
    maxP = 0
    while r < len(nums):
        if nums[l] < nums[r]:
            profit = nums[r] - nums[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r+=l 
    return maxP



