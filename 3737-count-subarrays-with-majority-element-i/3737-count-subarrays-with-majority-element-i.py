from typing import List


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 2
        size = 2 * n + 5
        bit = FenwickTree(size)

        prefix_sum = 0
        answer = 0

        bit.add(offset, 1)

        for num in nums:
            if num == target:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            current_index = prefix_sum + offset

            answer += bit.query(current_index - 1)

            bit.add(current_index, 1)

        return answer