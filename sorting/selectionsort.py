def SelectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        minindex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr
