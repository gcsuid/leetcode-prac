def lcs(nums):
    if not nums:
        return 0
    maxc = 1
    curc = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            curc += 1
            maxc = max(maxc, curc)
        else:
            curc = 1
    return maxc

nums = list(map(int, input("enter numbers separated by spaces: ").split()))
print(lcs(nums))
