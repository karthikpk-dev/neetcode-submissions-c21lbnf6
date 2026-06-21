class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set()
        visiting=set()
        preMap = {i : [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)


        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True
        
        for i in range(numCourses-1):
            if not dfs(i):
                return False
        return True