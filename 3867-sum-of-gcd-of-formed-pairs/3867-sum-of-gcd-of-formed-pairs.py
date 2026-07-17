import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        mxi = 0
        
        for i in range(n):
            mxi = max(mxi, nums[i])
            prefixGcd.append(math.gcd(nums[i], mxi))
        
        prefixGcd.sort()
        
        total = 0
        left, right = 0, n - 1
        while left < right:
            total += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total