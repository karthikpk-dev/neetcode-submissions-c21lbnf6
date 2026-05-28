class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res=[]
        def fun(i,sol):
            if i==len(nums):
                res.append(sol[:])
                return
            
            fun(i+1,sol)
            sol.append(nums[i])
            fun(i+1,sol)
            sol.pop()
        fun(0,[])
        return res