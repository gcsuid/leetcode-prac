def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

#example usage
'''if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubbleSort(arr)
    print("Sorted array is:", sorted_arr)'''

#if taking input from user
'''if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    
    sorted_arr = bubbleSort(arr)
    print("Sorted array is:", sorted_arr)'''


#without main and f strings in the input:
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = bubbleSort(arr)
print("Sorted array is:", sorted_arr)

