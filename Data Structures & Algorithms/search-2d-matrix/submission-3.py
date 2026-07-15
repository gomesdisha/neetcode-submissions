class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #scanning entire matrix at once using binary seacrh
        #basically consider the 2d matrix as a single 1d array
        #then m becomes the middle most element of the matrix(centre)
        #l and r is boundary, initally full matrix then reduce accordingly
        rows = len(matrix) #3
        cols = len(matrix[0])#4
        l,r = 0,rows*cols-1
        
        while l<=r:
            m = l + (r-l)//2 #5
            row = m//cols #5//4 = 1
            col = m%cols # 5%4= 1
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = m+1
            elif val>target:
                r = m-1
        return False
            
