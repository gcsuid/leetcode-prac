class solution:
    def sortColors(self, nums: list[int]) -> None:
        #using counting sort

        count = [0,0,0]
        for num in nums:
            count[num] += 1
        
        r,w,b = count
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w   
        nums[r+w:] = [2] * b
        