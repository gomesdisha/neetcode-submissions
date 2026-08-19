class Solution:
    def climbStairs(self, n: int) -> int:
        #Top down memoization
        memo = {1:1,2:2}
        #base cases are a lil different than normal fib, but its same idea

        def fib(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = fib(n-1) + fib(n-2)
                return memo[n]

        return fib(n)
        