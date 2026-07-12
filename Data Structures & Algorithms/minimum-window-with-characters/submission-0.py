class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tcnt = {}
        wincnt = {}
        l = 0

        for r in range(len(t)):
            tcnt[t[r]] = 1 + tcnt.get(t[r],0) 
            #update cnt of each ch in t
        
        have,need = 0,len(tcnt)
        res,reslen = [-1,-1], float("infinity")#to store substring indices and len

        for r in range(len(s)): #scan thru s and cmp have and  need
            wincnt[s[r]] = 1 + wincnt.get(s[r],0)

            if s[r] in tcnt and tcnt[s[r]]==wincnt[s[r]]:#check if el of s in t
                have += 1

            while have == need:
                #update results first:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen = r-l+1
                #shrink window from left by popping elements and moving pointer ->
                wincnt[s[l]] -= 1
                if s[l] in tcnt and tcnt[s[l]]>wincnt[s[l]]:
                    have -= 1 #checking the s popped element was in t asw
                l += 1
        l,r = res # l,r = [..,..]
        return s[l:r+1] if reslen != float("infinity") else ""



        
        