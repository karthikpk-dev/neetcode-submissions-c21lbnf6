class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        i=j=0
        m,n=len(s),len(t)

        if n==0:
            return ""
        countT= {}

        window={}
   

        for x in t:
            countT[x]=countT.get(x,0)+1

        have,need=0,len(countT)
        res,resLen=[-1,-1],float("inf")

        while j<m:
            window[s[j]]=1+window.get(s[j],0)
            if s[j] in countT and window[s[j]]==countT[s[j]]:
                have+=1
            
            while have == need:
                if (j-i+1)<resLen:
                    res=[i,j]
                    resLen=j-i+1

                window[s[i]]-=1
                if s[i] in countT and window[s[i]]<countT[s[i]]:
                    have-=1
                i+=1
            j+=1

        i,j=res
        return s[i:j+1] if resLen!=float("inf") else ""

