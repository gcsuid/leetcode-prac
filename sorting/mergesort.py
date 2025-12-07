def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    Left = mergeSort(arr[:mid]) 
    Right = mergeSort(arr[mid:])
    return merge(Left, Right)

def merge(Left, Right):
    sortedarr = []
    i = j = 0
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            sortedarr.append(Left[i])
            i += 1
        else:
            sortedarr.append(Right[j])
            j += 1
    while i < len(Left):
        sortedarr.append(Left[i])
        i += 1
    while j < len(Right):
        sortedarr.append(Right[j])
        j += 1
    return sortedarr

arr = list(map(int, input("enetr the numbers separated by spaces:").split()))
sortedarr = mergeSort(arr)
print("sorted array is:", sortedarr)
