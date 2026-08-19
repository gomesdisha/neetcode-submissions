class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp,minp,res = nums[0],nums[0],nums[0]

        for i in range(1,len(nums)):
            temp = maxp

            maxp = max(nums[i], nums[i]*maxp, nums[i]*minp)
            minp = min(nums[i], nums[i]*temp, nums[i]*minp)

            res = max(res,maxp)

        return res
        