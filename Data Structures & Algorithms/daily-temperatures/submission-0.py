class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #MONOTONIC STACK PROBLEM
        temp=temperatures
        tlen = len(temperatures)
        res = [0]*tlen
        stack = []#to store [temp,indices] of each temp
    
        for i,t in enumerate(temp):
            while stack and t > stack[-1][0]: #-1 is top ele, 0 gives temp, 1 gives index
                tem,idx = stack.pop()
                res[idx] = i-idx
            stack.append([t,i])
        return res

            

        