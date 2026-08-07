class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(path,i,psum):
            if psum == target:
                res.append(path[:])
                return
            if i>=len(nums) or psum>target:
                return

            path.append(nums[i])
            backtracking(path,i,psum+nums[i])

            path.pop()
            backtracking(path,i+1,psum)

        backtracking([],0,0)
        return res
        