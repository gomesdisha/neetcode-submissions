class TimeMap:
    def __init__(self):
        self.keyStore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]=[]
        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res,values  = "", self.keyStore.get(key,[])
        #values=[value][timestamp]
        l,r = 0, len(values)-1

        while l<=r:
            m = l+(r-l)//2 #m,l,r is index of the pair
            if values[m][1] <= timestamp: #[m][1] is value
                res = values[m][0] #[m][0] is timestamp
                l = m+1
            else:
                r = m-1
        return res


        
