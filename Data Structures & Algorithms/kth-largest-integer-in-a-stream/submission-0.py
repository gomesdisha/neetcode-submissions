import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify_max(self.nums)
        
    def add(self, val: int) -> int:
        lg = 0
        heapq.heappush_max(self.nums,val)
        #arr = self.nums #this doesnt make a copy its just a new pointer to the same heap
        arr = self.nums.copy()
        for i in range(self.k):
            lg = heapq.heappop_max(arr)
        return lg

        
