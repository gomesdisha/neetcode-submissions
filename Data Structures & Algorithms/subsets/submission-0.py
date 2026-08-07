class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(path,idx):
            if idx==n:
                res.append(path[:])
                return
            
            path.append(nums[idx])
            backtracking(path,idx+1)
            path.pop()

            backtracking(path,idx+1)
            
        backtracking([],0)
        return res

        