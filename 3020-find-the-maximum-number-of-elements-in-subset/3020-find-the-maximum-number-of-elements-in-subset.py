from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Special case: 1^2 = 1
        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            while cur in freq and freq[cur] >= 2:
                length += 2
                cur *= cur

                if cur > 10**9:
                    break

            # middle element needs only 1 occurrence
            if cur in freq:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans