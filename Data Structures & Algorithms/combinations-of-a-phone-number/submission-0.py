class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res=[]
        if not digits:
            return res
        n=len(digits)
        sol=''
        def dfs(ind):
            nonlocal sol,res
            if ind==n:
                res.append(sol[:])
                return

            char = digits[ind]
            for x in digitToChar[char]:
                sol+=x
                dfs(ind+1)
                sol=sol[:-1]
        dfs(0)
        return res



        