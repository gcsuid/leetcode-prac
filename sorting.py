l = [-5,2,1,3,7,2,8,4,3,6]

# bubble sort,inplace, stable, o(n^2), o(1)

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                flag = True

print('Before sorting:', l)
bubble_sort(l)
print('After using bubble sort:', l)


#insertion sort, inplace, stable, o(n^2), o(1) 
# from unsorted part, pick one element and insert it into the sorted part


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
print('Before sorting:', l)
insertion_sort(l)
print('After using bubble sort:', l)


#selection sort, inplace, unstable, o(n^2), o(1)
# from unsorted part, pick the smallest element and swap it with the first element of uns

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


#merge sort, not inplace, stable, o(n log n), o(n)
# divide and conquer, divide the array into two halves, sort them and merge them since its recurisve


def merge_sort(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr 
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result



#quick sort, inplace, unstable, o(n log n) average, o(n^2) worst, o(log n) space
# divide and conquer, pick a pivot, partition the array around the pivot, sort the partitions

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]
    left = [x for x in arr[:-1] if x <= p]
    right = [x for x in arr[:-1] if x > p]
    
    l = quick_sort(left)
    r = quick_sort(right)
    return l + [p] + r



#counting sort, not inplace, stable, o(n+k), o(k) space, k is the range of the input
# count the occurrences of each element, then reconstruct the sorted array, only when k is small

def counting_sort(arr):
    if not arr:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1
    result = []
    for i in range(k):
        result.extend([i + min_val] * count[i])
    return result


