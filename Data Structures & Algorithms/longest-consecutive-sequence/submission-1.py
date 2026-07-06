class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num-1) not in numSet:
                length = 1 #beginning element
                while (num+length) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
        
        """res = {}
        nums.sort()
        #length = 0

        for i in range(len(nums)-1):
            if (nums[i+1] - nums[i] == 1):
                res.add(nums[i])
                res.add(nums[i+1])

        return len(res)"""


        