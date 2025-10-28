a = [1,2,3,4,5,6,7,8,9]

# two pointer approach for list reversal
'''p,q = 0, len(a)-1


def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    
while p < q:
    swap(a, p,q)
    p += 1
    q -= 1   

print(a)'''
#print(a[::-1])  # Using slicing to reverse the list 

slice = [1,2,3,4,5]
print(slice[1:5:2])  # Output: [2, 4]

#reverse string in python
def reverse_string(s):
    return s[::-1]

#or

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

