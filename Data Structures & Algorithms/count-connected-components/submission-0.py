class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited=set()
        cnt=0
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nxt in adj[i]:
                dfs(nxt)
            return


        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt+=1
        return cnt