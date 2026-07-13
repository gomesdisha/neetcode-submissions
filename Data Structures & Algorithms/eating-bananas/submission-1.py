class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)#[1,2,3..25]
        #piles = [25,10,23,4]

        while l<=r:
            hrs=0
            mid = l+((r-l)//2)
            for i in range(len(piles)):
                """while piles[i]>0:#cant modify og data will work on wrong values in next loopp
                    piles[i] -= mid
                    hrs+=1"""
                #hrs+= (piles[i]+mid-1)//mid 
                hrs+= math.ceil(piles[i]/mid) 
                #round figure to up
            if hrs>h:
                l=mid+1
            elif hrs<=h:
                r=mid-1
                ans=mid
        return ans



        