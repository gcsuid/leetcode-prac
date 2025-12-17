def containsduplicate(nums):
    nums.sort()
    charset = set()
    for i in nums:
        if i in charset:
            return True
        else:
            charset.add(i)
    return False

# Example usage:
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(containsduplicate(nums))