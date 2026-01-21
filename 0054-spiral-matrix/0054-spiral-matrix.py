class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
                if matrix:
                    res += matrix.pop()[::-1]
                for row in reversed(matrix):
                    if row and matrix:
                        res.append(row.pop(0))
        return res
