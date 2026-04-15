class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        i,j=0,n-1
        def isPal(i,j,s):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        while i < j:
            if s[i]!=s[j]:
                return isPal(i+1,j,s) or isPal(i,j-1,s)
            i+=1
            j-=1
        return True

