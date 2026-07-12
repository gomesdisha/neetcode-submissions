class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = l = maxf = 0 
        cnt = {}
        #AABCDBA

        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r],0)
            maxf = max(cnt[s[r]],maxf)

            while (r-l+1) - maxf > k:
                cnt[s[l]] -= 1
                l+=1
            
            res = max(res, r-l+1) #r-l+1 is window size
        return res


                

        

        