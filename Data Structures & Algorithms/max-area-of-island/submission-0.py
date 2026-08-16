class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        m,n = len(grid),len(grid[0])

        def dfs(i,j): #checks one single island at a time
            nonlocal ar
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!= 1:
                return
            else:
                ar+=1
                grid[i][j]=0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                ar = 0
                if grid[i][j] == 1:
                    dfs(i,j)
                    area = max(ar,area)
        return area


        