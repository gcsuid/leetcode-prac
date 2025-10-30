class solution:
    def majority2(self, nums):
        n = len(nums)
        res = []
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        for key, value in dictionary.items():
            if value > n // 3:
                res.append(key)
        return res