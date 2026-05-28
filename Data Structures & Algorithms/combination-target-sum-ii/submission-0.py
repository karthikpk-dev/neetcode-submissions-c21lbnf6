class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        n=len(candidates)
        def dfs(ind,sum,path):
            if sum==target:
                res.append(path[:])
                return


            for i in range(ind,n):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if sum + candidates[i] >target:
                    break
                path.append(candidates[i])
                dfs(i+1,sum+candidates[i],path)
                path.pop()
        dfs(0,0,[])
        return res