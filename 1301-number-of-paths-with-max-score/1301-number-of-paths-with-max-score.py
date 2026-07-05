from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7
        n = len(board)

        # best[r][c] = max score to reach (r, c)
        # ways[r][c] = number of ways to get that max score
        best = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        best[0][0] = 0
        ways[0][0] = 1

        for r in range(n):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                if board[r][c] == 'X':
                    continue

                max_prev = -1
                count = 0

                for pr, pc in ((r - 1, c), (r, c - 1), (r - 1, c - 1)):
                    if 0 <= pr < n and 0 <= pc < n and best[pr][pc] != -1:
                        if best[pr][pc] > max_prev:
                            max_prev = best[pr][pc]
                            count = ways[pr][pc]
                        elif best[pr][pc] == max_prev:
                            count = (count + ways[pr][pc]) % mod

                if max_prev == -1:
                    continue

                cell = board[r][c]
                value = 0 if cell == 'S' else int(cell)
                best[r][c] = max_prev + value
                ways[r][c] = count

        if best[n - 1][n - 1] == -1:
            return [0, 0]

        return [best[n - 1][n - 1] % mod, ways[n - 1][n - 1]]