class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj=defaultdict(list)
        for i,e in enumerate(equations):
            u,v=e[0],e[1]
            adj[u].append((v,values[i]))
            adj[v].append((u,1/values[i]))
        visited=set()
        
        def dfs(source,target,product):
            if source not in adj or target not in adj:
                return -1
            visited.add(source)
            if source==target:
                return product
            for nei in adj[source]:
                u,v=nei
                if u not in visited:
                
                    ans=dfs(u,target,product*v)
                    if ans!=-1:
                        return ans
            visited.remove(source)     
            return -1

        res=[]
        for x in queries:
            u,v=x[0],x[1]
            visited=set()
            res.append(dfs(u,v,1)) 
        return res

