def rev(arr):
    return arr[::-1]

def rev_arr(arr):
    return list(reversed(arr))

def rev_array(arr):
    n= len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] =  arr[n-i-1], arr[i] 
    return arr

def rev_arrayy(arr):
    n= len(arr)
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        new_arr.append(arr[i])
    return arr

def re_arr(arr):
    n = len(arr)
    start, end = 0, n-1
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]        
        start+=1
        end-=1
    return arr

from functools import reduce

def rev_arr_red(arr):
    rev_arr_temp = reduce(lambda acc, x:[x]+acc, arr, [])
    return rev_arr_temp

print(rev_arr_red([3, 2, 5, 23, 7, 9]))

def rev_recursive(arr, start, end):
    if start <= end:
        return
    temp_arr = rev_recursive(arr, start+1, end-1)

def rev_stack(arr):
    n=len(arr)
    rev_arr = []
    stack = arr[:]
    while stack:
        rev_arr.append(stack.pop())
    return rev_arr
        
rev_stack([3, 5, 3, 1, 7, 9])

def rev_arrr(arr):
    n=len(arr)
    i=0
    while i< n//2:
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        i+=1
    return arr



# print(rev([3, 2, 4, 1, 6, 7]))
# print(rev_arr([3, 2, 4, 1, 6, 7]))
print(rev_array([3, 2, 4, 1, 6, 7]))
print(rev_arrr([3, 2, 4, 1, 6, 7]))
