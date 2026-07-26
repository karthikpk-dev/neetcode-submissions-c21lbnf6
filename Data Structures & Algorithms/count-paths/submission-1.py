class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def fun(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]

            d = fun(i+1,j)
            r = fun(i,j+1)
            memo[(i,j)]= d + r
            return memo[(i,j)]
        return fun(0,0)