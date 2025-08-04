# variable sliding window without repeating the characters

def lengthOfmax_avgSubstring(s):
    l = 0
    max_avg = 0
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        w = (r-l)+1
        max_avg = max(max_avg, w)
        sett.add(s[r])

    return max_avg


# fixed length sliding window

def max_average_subarray(nums, k):
    l = 0
    r = k-1
    max_avg = 0.0
    n= len(nums)
    if k > n:
        return None
    for i in range(0, n-k+1):
        cal_sum = sum(nums[i:i+k]) #O(K)
        avg = cal_sum/k
        max_avg = max(avg, max_avg)
        r+=1
        l+=1

    return max_avg

print(max_average_subarray([1, 12, -5, -6, 50, 3], 4))


# prefix sum array

def max_average(nums, k):
    n= len(nums)
    if k > n:
        return None
    ps = [0]* (n+1)
    for i in range(n):
        ps[i+1] = ps[i]+nums[i]
    
    max_avg = float('-inf')
    for i in range(0, n-k+1):
        window_sum = ps[i+k] - ps[i]
        max_avg = max(max_avg, window_sum / k)

    return max_avg

print(max_average([1, 12, -4, -7, 12, 17], 4))



#sliding window inplace

def max_avg_sliding(nums, k):
    n= len(nums)
    if k > n:
        return None
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += nums[i] - nums[i-k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum / k

print(max_avg_sliding([1,12, -5, -6, 50, 3], 4))


# Using numpy

import numpy as np

def max_average_numpy(nums, k):
    arr = np.array(nums, dtype=np.float64)
    window_sums = np.convolve(arr, np.ones(k, dtype=np.float64), mode='valid')
    return np.max(window_sums)/k

print(max_average_numpy([1,12, -5, -6, 50, 3], 4))
