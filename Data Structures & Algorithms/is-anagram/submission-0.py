class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = "".join(sorted(s))
        char_t = "".join(sorted(t))
        
        if char_s != char_t:
            return False
        return True
        
