class MinStack:
    #works but not O(1). Good thing tho i kinda learnt how to use fns in py
    def __init__(self):
        self.stack = []
        self.tops=0
        self.minm = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,(self.minm[self.tops-1] if self.minm else val))
        self.minm.append(val)
        self.tops += 1
        
    def pop(self) -> None:
        self.stack.pop()
        self.minm.pop()
        self.tops-=1
    
    def top(self) -> int:
        return self.stack[self.tops-1]

    def getMin(self) -> int:
        """minm=float("inf")
        for i in range(self.tops-1,-1,-1):
            minm = min(minm,self.stack[i])
        return int(minm)"""
        return self.minm[self.tops-1]

        
