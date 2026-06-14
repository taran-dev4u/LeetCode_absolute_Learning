from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []

        for word in words:
            total_weight = 0
            for char in word:
                total_weight += weights[ord(char) - ord('a')]

            mapped_value = total_weight % 26
            result.append(chr(ord('z') - mapped_value))

        return "".join(result)