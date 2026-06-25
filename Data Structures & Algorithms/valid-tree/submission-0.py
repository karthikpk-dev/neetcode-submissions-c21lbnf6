class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited=set()


        def dfs(i,pre):

            if i in visited:
                return True


            visited.add(i)
            for nxt in adj[i]:
                if nxt == pre:
                    continue
                if nxt in visited:
                    return False
                if not dfs(nxt,i):
                    return False
       
            
            return True

        if not dfs(0,-1):
                return False
        return len(visited)==n
        


