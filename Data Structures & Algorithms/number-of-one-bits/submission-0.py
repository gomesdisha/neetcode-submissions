class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(bin(n)[2:])
        res = 0

        for d in binary:
            if d == "1":
                res+=1
        
        return res