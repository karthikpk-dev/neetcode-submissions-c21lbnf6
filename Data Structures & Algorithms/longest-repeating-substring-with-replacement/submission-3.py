class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        i=j=0
        n=len(s)
        map ={}
        maxi=0
        while j<n:
            map[s[j]]=map.get(s[j],0)+1
            maxi=max(maxi,map[s[j]])
            
            while j-i+1-maxi > k:
                map[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
            j+=1
            
                
        return res