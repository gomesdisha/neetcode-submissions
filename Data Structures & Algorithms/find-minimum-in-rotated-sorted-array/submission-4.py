class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        #sm = float("infinity")

        while l<r:
            mid=l+(r-l)//2
            if nums[r]>nums[mid]:
                r = mid
            else:
                l = mid+1
            #sm = min(sm,nums[mid])
        #return int(sm)
        return nums[l]
