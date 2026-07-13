class Solution:
    def isValid(self, s: str) -> bool:
        closeTOopen = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s:
            if c in closeTOopen:
                if stack and stack[-1]==closeTOopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        

        
    


        
        