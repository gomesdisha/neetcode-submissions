class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:#this one for the outer var other than 2 pointer
                continue
            
            l,r = i+1, len(nums)-1
            while l<r:
                tsum = n+nums[l]+nums[r]
                if tsum > 0:
                    r-=1
                elif tsum < 0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:#this one for the 2 pointer
                        l+=1
        return res

        