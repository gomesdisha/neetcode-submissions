class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        clen = len(matrix[0])
        #len(matrix[0][0]) is a number not row , so only matrix[0] will give row 0

        for r in range(len(matrix)):
            for c in range(clen):
                n = matrix[r][c]
                if target == n:
                    return True
                elif target == matrix[r][clen-1]:
                    return True
                elif n<target<matrix[r][clen-1]:
                    continue
                else:
                    break
        return False





        