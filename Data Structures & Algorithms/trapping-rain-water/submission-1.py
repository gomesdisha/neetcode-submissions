class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0]*len(height)
        rmax = [0]*len(height)
        waterpos = [0]*len(height)
        sol = 0
        lmax[0] = height[0]
        rmax[-1] = height[-1]

        for i in range(1,len(height)):
            lmax[i] = max(height[i],lmax[i-1])

        for i in range(len(height)-2,-1,-1):
            rmax[i]= max(height[i],rmax[i+1])

        for i in range(len(height)):
            waterpos[i]=min(lmax[i],rmax[i])

            if waterpos[i]-height[i] > 0:
                sol+=waterpos[i]-height[i]

        return sol
        
        
        

