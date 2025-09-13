from typing import List
def generatePascals(nums: int) -> List[List[int]] : 
    tri = []
    for r in range(nums):
        row = [1]*(nums+1)
        for c in range(1, r):
            row[c] = tri[-1][c-1]+tri[-1][c]
        tri.append(row)
    return tri


def kth_pascals_row(k:int) -> List[int]:
    row = [1]
    for r in range(1, k+1):
        row.append(1)
        for c in range(r-1, 0, -1):
            row[c] = row[c] + row[c-1]
    return row 