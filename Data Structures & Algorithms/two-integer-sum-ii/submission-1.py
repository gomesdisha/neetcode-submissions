class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r= 0,len(numbers)-1
        while l<r:
            csum= numbers[l]+numbers[r]
            if csum == target:
                return [l+1,r+1]
            if target>csum:
                l+=1
            if target<csum:
                r-=1
        
