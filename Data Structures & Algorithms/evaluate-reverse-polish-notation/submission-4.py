class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #POSTFIX problem
        stack = []
        ans = 0
        ops= ["+","-","/","*"]
        
        for i in range(len(tokens)):
            ch = tokens[i]
            if ch not in ops:
                stack.append(int(ch))
            if ch == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                ans = val1+val2
                stack.append(ans)
            elif ch == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                ans = val1*val2
                stack.append(ans)
            elif ch == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                ans = val2-val1
                stack.append(ans)
            elif ch == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                ans = int(val2/val1)
                stack.append(ans)
        return stack[-1]


            

        