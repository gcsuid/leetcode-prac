class solution:
    def longestsubsstringwithoutcharacters(self,nums):
        l = 0
        maxl = 0
        charset = set()

        for r in range(len(nums)):
            while nums[r] in charset:
                charset.remove(nums[l])
                l += 1
            charset.add(nums[r])
            maxl = max(maxl, r - l + 1)
        return maxl
