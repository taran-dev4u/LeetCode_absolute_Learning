def selectionSort(arr):
    n= len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [4, 3, 26, 12, 27, 5]
print(selectionSort(arr))