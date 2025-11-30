class soluton:
    def minSubaraay(self,nums, target):
/
        l = 0
        cs = 0
        minl = float('inf')

        for r in range(len(nums)):
            cs += nums[r]

            while cs >= target:
                minl = min(minl, r-l+1)
                cs -= nums[l]
                l += 1
        return minl if minl != float('inf') else 0