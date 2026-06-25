class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans=[]
        preMap={i : [] for i in range(numCourses)}
        for i,j in prerequisites:
            preMap[j].append(i)
        visited=set()
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            #prereq of i == j?
            for nxt in preMap[i]:
                if nxt==j or dfs(nxt,j):
                    memo[(i,j)]=True
                    return True
            memo[(i,j)]=False
            return False


        for u,v in queries:
            ans.append(dfs(v,u))
        return ans