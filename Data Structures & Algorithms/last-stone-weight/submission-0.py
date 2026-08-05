import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stone_maxheap = heapq.heapify_max(stones)
        heapq.heapify_max(stones)
        while len(stones)>1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x==y:
                #destroy stones
                continue
            elif x>y: #not x<y, because x will never be smaller than y
                #remove x, add y-x
                #y is the second, x is the first largest/ both equal
                heapq.heappush_max(stones, x-y)
        return stones[0] if len(stones)!=0 else 0
        
        