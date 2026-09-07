class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        residx = 0

        for i in range(len(s)):
            #odd palindrome check from i as centre
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    residx = l
                    reslen = r-l+1 #r-l+1 is the substring len
                l-=1
                r+=1
                
            #even palindrome check from i as centre
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    residx = l
                    reslen = r-l+1
                l-=1
                r+=1

        return s[residx:residx+reslen]
            
        