# Continuous subarray Problem.

def continuousArray(nums, k):
    mp  = {0:-1}
    s = 0
    for i, x in enumerate(nums):
        s+=x
        if k !=0:
            s%=k
        if s in mp:
            i0 = mp[s]
            length = j-i0
            if





