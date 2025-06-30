def bubblesort(arr):
    n = len(arr)
    print(arr)
    cnt = 0
    for i in range(n):
        swapped = False  
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            cnt+=1
        # if not swapped:
        #     break
    print(cnt)
    return arr

arr = [9, 8, 7, 6, 5]

print(bubblesort(arr))
