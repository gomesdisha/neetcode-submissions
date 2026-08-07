class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """nums = set()
        for c in candidates:
            nums.add(c)"""
        candidates.sort() #adding this made 23/25 pass, TLE
        #makes easier to skip dups since dups next to each other
        res = []
        def backtrack(path,i,psum):
            #if psum == target and path[:] not in res:
            #we need to avoid dups instead of removing here
            if psum == target:
                res.append(path[:])
                return
            if psum>target or i>=len(candidates):
                return
            
            for j in range(i,len(candidates)):
                #skips duplicates: i is the og val, j is dup val 
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                    
                path.append(candidates[j])
                backtrack(path,j+1,psum+candidates[j])

                path.pop()
                #backtrack(path,i+1,psum)

        backtrack([],0,0)
        return res



        