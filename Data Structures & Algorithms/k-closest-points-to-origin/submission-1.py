class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        #heapq.heapify_max(heap)
        
        for x,y in points:
            dist = (x**2 + y**2)
            heapq.heappush_max(heap, (dist,(x,y)))
        
            if len(heap)>k:
                heapq.heappop_max(heap)
        
        
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res



        