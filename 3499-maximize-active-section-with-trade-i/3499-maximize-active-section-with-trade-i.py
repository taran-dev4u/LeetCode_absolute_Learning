class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")
        zero_blocks = []
        i = 0

        while i < len(s):
            if s[i] == "1":
                i += 1
            else:
                count = 0

                while i < len(s) and s[i] == "0":
                    count += 1
                    i += 1

                zero_blocks.append(count)

        max_gain = 0

        for i in range(1, len(zero_blocks)):
            max_gain = max(
                max_gain,
                zero_blocks[i - 1] + zero_blocks[i]
            )

        return ones + max_gain