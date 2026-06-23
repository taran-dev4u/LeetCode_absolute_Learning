class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        up = [0] * m
        down = [0] * m

        for i in range(m):
            up[i] = i              # previous value smaller than i
            down[i] = m - 1 - i    # previous value greater than i

        for _ in range(2, n):
            prefix_down = [0] * (m + 1)
            prefix_up = [0] * (m + 1)

            for i in range(m):
                prefix_down[i + 1] = (prefix_down[i] + down[i]) % mod
                prefix_up[i + 1] = (prefix_up[i] + up[i]) % mod

            new_up = [0] * m
            new_down = [0] * m

            for i in range(m):
                # previous value < current value
                new_up[i] = prefix_down[i]

                # previous value > current value
                new_down[i] = (prefix_up[m] - prefix_up[i + 1]) % mod

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % mod