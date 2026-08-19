class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = float("-inf")
        curs = 0

        for i in range(len(nums)):
            curs+=nums[i]
            maxs = max(curs,maxs)

            if curs<0:
                curs = 0

        return maxs
        