class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        heapq.heapify_max(heap)
        #dist b/w (x1,y1) and (0,0):
        #sqrt((x1)^2 + (y1)^2)
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = (x**2 + y**2)
            #dist = math.sqrt (x**2 + y**2)
            #no need to to sqrt just this also enough (x**2 + y**2)
            heapq.heappush_max(heap, (dist,(x,y)))
        
        while len(heap)>k:
            heapq.heappop_max(heap)
        
        #they asked K CLOSEST POINTS, not Kth!!
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res



        