class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo={}
        def f(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            if n in memo:
                return memo[n]

            memo[n]=(f(n-1)+f(n-2)+f(n-3))
            return memo[n]
        return f(n)