class Solution:
    def isPalindrome(self, s: str) -> bool:
        res="".join(x.lower() for x in s if x.isalnum())
        
        n=len(res)
        i,j=0,n-1

        def fun(i,j,res):
            if i<j:
                if res[i]!=res[j]:
                    return False
                return fun(i+1,j-1,res)
            return True
        
        return fun(i,j,res)