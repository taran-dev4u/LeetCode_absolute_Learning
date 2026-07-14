from typing import List
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_value = max(nums)

        # dp[g1][g2] = number of assignments producing these two GCDs
        dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
        dp[0][0] = 1

        for num in nums:
            next_dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]

            for g1 in range(max_value + 1):
                for g2 in range(max_value + 1):
                    ways = dp[g1][g2]

                    if ways == 0:
                        continue

                    # Choice 1: Do not place num in either subsequence
                    next_dp[g1][g2] = (
                        next_dp[g1][g2] + ways
                    ) % MOD

                    # Choice 2: Place num in seq1
                    new_g1 = gcd(g1, num)
                    next_dp[new_g1][g2] = (
                        next_dp[new_g1][g2] + ways
                    ) % MOD

                    # Choice 3: Place num in seq2
                    new_g2 = gcd(g2, num)
                    next_dp[g1][new_g2] = (
                        next_dp[g1][new_g2] + ways
                    ) % MOD

            dp = next_dp

        answer = 0

        # g starts at 1 because both subsequences must be non-empty.
        for g in range(1, max_value + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer