class Solution:
    def maxArea(self, heights: List[int]) -> int:
        fin=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                fin = max(fin, min(heights[i],heights[j])*(j-i))
        return fin

        