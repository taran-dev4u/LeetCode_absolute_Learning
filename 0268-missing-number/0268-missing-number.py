class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1) // 2

        actual_sum = sum(nums)
        return expected_sum - actual_sum





    # def missingNumber(self, nums: List[int]) -> int:

    #     n= len(nums)
    #     nums_set = set(nums)

    #     for num in range(n+1):
    #         if num not in nums_set:
    #             return num
        


        

        
        