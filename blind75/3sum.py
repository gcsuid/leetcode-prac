def threeSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n):
        if nums[i] == nums[i-1]:
            continue
        l,r = i + 1, n - 1
        while l < r:
            ts = nums[i] + nums[l] + nums[r]
            if ts > target:
                r -= 1
            elif ts < target:
                l += 1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                while l < r and nums[i] == nums[i-1]:
                    l += 1
    return res


li = map(list(int, input("enter something separated by:").split()))
print(threeSum(li))
            
