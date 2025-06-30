def insertionSort(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr


arr = [3, 25, 1, 6, 15, 89, 32]
print(insertionSort(arr))
