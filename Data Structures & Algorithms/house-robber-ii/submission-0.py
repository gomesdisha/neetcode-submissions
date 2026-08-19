class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n ==2:
            return max(nums[0],nums[1])
        if n==3:
            return max(nums[0],nums[1],nums[2])

        def robbery(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            prev,cur = arr[0],max(arr[0],arr[1])

            for i in range(2,n):
                prev,cur=cur,max(cur,prev+arr[i])

            return cur

        #start from first house,skip last house:
        first = robbery(nums[:-1])
        #start from last house,skip first house:
        last = robbery(nums[1:])

        return max(first,last)

        

        
        
        