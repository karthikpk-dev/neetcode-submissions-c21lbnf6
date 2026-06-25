class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        preMap={i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[pre].append(crs) #adjacency list
        visited=set()
        visiting=set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visited.add(crs)
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            ans.append(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
            
        ans.reverse()
        return ans
        