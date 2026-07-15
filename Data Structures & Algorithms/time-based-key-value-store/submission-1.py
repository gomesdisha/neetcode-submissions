class TimeMap:
    def __init__(self):
        self.keyStore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]=[] #need to create empty list to store value,times pairs
        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res,values  = "", self.keyStore.get(key,[])#if some random timeMap.get("abc", 1); is done, and abc not in keyStore, then default is []
        #values=[value][timestamp]
        l,r = 0, len(values)-1

        if key not in self.keyStore:
            return ""

        while l<=r:
            m = l+(r-l)//2 #m,l,r is index of the pair
            if values[m][1] <= timestamp: #[m][1] is value
                res = values[m][0] #[m][0] is timestamp
                l = m+1
            else:
                r = m-1
        return res


        
