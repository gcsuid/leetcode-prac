def subarraySum(self, nums: list[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_sums = {0: 1}

    for num in nums:
        prefix_sum += num
        diff = prefix_sum - k
        if diff in prefix_sums:
            count += prefix_sums[diff]
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
    return count