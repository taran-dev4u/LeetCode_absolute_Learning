from typing import List

def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    zr, zc = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zr.add(i); zc.add(j)
    for i in range(m):
        for j in range(n):
            if i in zr or j in zc:
                matrix[i][j] = 0
    # print(matrix)


set_matrix_zeroes([[1,2,0],[3,2,6],[7,9,4]])


def set_matrix_zeroes_sec(matrix:List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    first_row = any(matrix[0][x] == 0 for x in range(m))
    first_col = any(matrix[j][0] == 0 for j in range(n))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
            
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_col:
        for i in range(m):
            matrix[i][0] = 0

    if first_row:
        for j in range(n):
            matrix[0][j] = 0
    print(matrix)

set_matrix_zeroes_sec([[1,2,0],[3,5,6],[7,9,4]])