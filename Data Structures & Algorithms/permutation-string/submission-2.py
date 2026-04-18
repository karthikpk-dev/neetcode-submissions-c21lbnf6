class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if m > n:
            return False
        map1={}
        map2={}
        for j in range(m):
            map1[s1[j]]=map1.get(s1[j],0)+1
            map2[s2[j]]=map2.get(s2[j],0)+1
        j=m
        i=0
        while j<n:
            if map1==map2:
                return True
            map2[s2[j]]=map2.get(s2[j],0)+1
            map2[s2[i]]=map2.get(s2[i],0)-1
            if map2[s2[i]]==0:
                del map2[s2[i]]
            j+=1
            i+=1
        return map1==map2

            
