class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        i=j=0
        n=len(s)
        count=set()
 
        while j<n:
            while s[j] in count:
                count.remove(s[i])
                i+=1
                
                       
            
            res=max(res,j-i+1)
            count.add(s[j])
            j+=1
                
        return res