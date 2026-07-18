from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_value = max(nums)

        frequency = [0] * (max_value + 1)
        for number in nums:
            frequency[number] += 1
        exact_gcd = [0] * (max_value + 1)

        for divisor in range(max_value, 0, -1):
            divisible_count = 0

            for multiple in range(divisor, max_value + 1, divisor):
                divisible_count += frequency[multiple]

            pair_count = divisible_count * (divisible_count - 1) // 2

            for multiple in range(divisor * 2, max_value + 1, divisor):
                pair_count -= exact_gcd[multiple]

            exact_gcd[divisor] = pair_count

        cumulative = [0] * (max_value + 1)
        for gcd_value in range(1, max_value + 1):
            cumulative[gcd_value] = (
                cumulative[gcd_value - 1] + exact_gcd[gcd_value]
            )

        answer = []

        for query in queries:
            gcd_value = bisect_right(cumulative, query)
            answer.append(gcd_value)

        return answer