from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0,0
        q = deque()
        rows,cols = len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1: #counts intial fresh oranges
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c)) #adds initial rotten oranges to queue
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]] #to check all 4 sides 

        while q and fresh>0 :
            length = len(q)#stores rotten oranges at time t
            for i in range(length): #need to run for time t rotten only, not additional added rotten oranges
                row,col = q.popleft() #coordinate of each rotten
                for dr,dc in directions: #check all 4 sides of 1 rotten orange
                    r,c = dr+row,dc+col #pivot to a side

                    if(r<0 or c<0 or r==rows or c==cols or grid[r][c] != 1):
                        continue 

                    #executes only if grid[r][c]==1
                    grid[r][c] = 2 #make side rotten
                    q.append((r,c)) #append the new rotten
                    fresh -= 1 #dec total fresh
            time+=1
        
        return time if fresh == 0 else -1
                    



        