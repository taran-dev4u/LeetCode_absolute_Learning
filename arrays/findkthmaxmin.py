# slicing
# def find_kth_max_minslice(arr, k):
#     n=len(arr)
#     arr.sort()
#     min = arr[k-1]
#     max = arr[-k]
#     print(arr, min, max)

# find_kth_max_minslice([3, 4, 2, 1, 8, 6, 0], 2)
    
def find_kth_max_min(arr, k):
    n= len(arr)
    arr.sort()
    for i in range(n):
        if i == k:
            mini = arr[i]
            maxi = arr[n-i-1]
    print(mini, maxi)

find_kth_max_min([73, 21, 86, 38, 93, 65], 2)



def find_kth_min_max(arr):
    n= len(arr)
        
        