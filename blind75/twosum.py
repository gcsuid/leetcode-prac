def twosum(nums, k):
    map = {}
    for i, val in enumerate(nums):
        comp = k - val
        if comp in map:
            return [map[comp], i]
        else:
            map[val] = i

#eexample usge
l = map(list(int,input("Enter numbers separated by spaces:").split()))
k = int(input("Enter the target sum: "))
print(twosum(l,k))