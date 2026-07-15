class MinStack:

    def __init__(self):
        self.stack = []
        self.tops=0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.tops += 1
        
    def pop(self) -> None:
        self.stack.pop()
        self.tops-=1
    
    def top(self) -> int:
        return self.stack[self.tops-1]

    def getMin(self) -> int:
        minm=float("infinity")
        for i in range(self.tops-1,-1,-1):
            minm = min(minm,float(self.stack[i]))
        return int(minm)

        
