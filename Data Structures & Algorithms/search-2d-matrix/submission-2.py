class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rlen = len(matrix)
        clen = len(matrix[0])

        for r in range(rlen):
            if matrix[r][0]<=target<=matrix[r][clen-1]:
                l,ri=0,clen-1
                while l<=ri:
                    m =l + (ri - l) // 2
                    if matrix[r][m] == target:
                        return True
                    elif matrix[r][m]>target:
                        ri = m-1
                    else:
                        l = m+1
        return False





        