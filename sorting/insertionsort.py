def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # place key in correct position
    return arr


arr = list(map(int,input("enter the separated values:").split()))
sorted_arr = insertionSort(arr)
print("sorted array is:", sorted_arr)
