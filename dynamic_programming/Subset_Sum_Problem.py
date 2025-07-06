def subSetSumRec(arr, n, S):
    if S == 0:
        return True
    if n==0:
        return False
    
    if arr[n-1] > S:
        return subSetSumRec(arr, n-1, S)
    
    return (subSetSumRec(arr, n-1, S) or subSetSumRec(arr, n-1, S-arr[n-1]))


def subsetSumRecMemo(arr, n, S, memo=None):
    if memo is None:
        memo = {}
    if S == 0:
        return True
    if n == 0:
        return False

    if (n, S) in memo:
        return memo[(n, S)]
        
    if arr[n-1] > S:
        memo[(n, S)] = subsetSumRecMemo(arr, n-1, S)
    
    else: 
        memo[(n, S)] = subsetSumRecMemo(arr, n-1, S, memo) or
        subsetSumRecMemo(arr, n-1, S-arr[n-1], memo)

    return memo[(n, S)]


def subSetSumTab(arr, S):
    n = len(arr)
    dp = [[False]*(S+1) for _ in range(n+1)]
