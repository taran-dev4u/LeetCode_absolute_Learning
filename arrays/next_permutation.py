from typing import List, Tuple
def next_permutation(nums : List[int]) -> int :
    n = len(nums)
    i = n-2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i == -1:
        nums.reverse()
        return

    j = n-1
    while nums[j] <= nums[i]:
        j-=1
    nums[j] , nums[i] = nums[j], nums[i]

    l, r = i+1, n-1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1; r-=1b