class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[0]*(len(nums)-k+1)
        l = 0

        if k==1:
            return nums

        for r in range(k-1,len(nums)):
            p=l
            while p<=r:
                res[l]=max(res[l],nums[p])
                p+=1
            l+=1
        return res

        