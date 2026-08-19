class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #TOP DOWN 
        #base case
        n = len(cost)
        memo = {0:0,1:0}

        def min_cost(i):
            if i in memo:
                return memo[i]
            else:
                memo[i]= min(min_cost(i-1)+cost[i-1], min_cost(i-2)+cost[i-2])
                return memo[i]

        return min_cost(n)

        