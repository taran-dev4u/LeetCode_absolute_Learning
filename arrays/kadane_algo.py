def find_min_max(arr):
    min_ele = min(arr)
    max_ele = max(arr)
    print(min_ele, max_ele)

def find_min_max_ele(arr):
    for i in range(len(arr)):
        minn = arr[0]
        maxx = arr[0]
        if minn > arr[i]:
            minn = arr[i]
        if maxx < arr[i]:
            maxx = arr[i]
    print(minn, maxx)

find_min_max_ele([3, 1, 5, 7, 67, 2, 38])
find_min_max([68, 54, 21, 43, 25, 77])
from functools import reduce

def find_min_max_func(arr):
    minn = reduce(lambda a, b: a if a<b else b, arr)
    maxx = reduce(lambda a, b: a if a>b else b, arr)
    print(minn, maxx)

find_min_max_func([23, 45, 87, 12, 86, 378, 452])