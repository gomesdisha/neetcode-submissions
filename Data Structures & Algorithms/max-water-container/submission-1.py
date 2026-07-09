class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #heights.sort()
        #volume = width*height; width = r-l ; height = min(l,r)
        maxv = 0

        #for i,n in enumerate(heights):
        l,r = 0,len(heights)-1

        while l<r:
            height = min(heights[l],heights[r])
            width = r-l
            vol = height*width
            if vol>maxv:
                maxv=vol
            if heights[l]>heights[r]:
                r-=1
            elif heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return maxv
            
            




        
        