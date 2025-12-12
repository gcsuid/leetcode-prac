def quickSort(arr):
    if len(arr) <= 1:
        return arr  # Base case — already sorted
    
    pivot = arr[-1]  # Choose the last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quickSort(left) + [pivot] + quickSort(right)

    


# Example usage
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = quickSort(arr)
print("Sorted array is:", sorted_arr)
