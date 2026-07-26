class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Three largest numbers
        max1 = float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")

        min1 = float("inf")
        min2 = float("inf")

        for num in nums:

            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num <= min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        product_of_three_largest = max1 * max2 * max3
        product_with_two_negatives = min1 * min2 * max1

        return max(product_of_three_largest, product_with_two_negatives)