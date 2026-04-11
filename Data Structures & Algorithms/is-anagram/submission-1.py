class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1,n2=len(s),len(t)
        if n1!=n2:
            return False
        
        dictt = {}

        for x in s:
            dictt[x]= dictt.get(x,0)+1
        for x in t:
            dictt[x] = dictt.get(x,0)-1
        
        for value in dictt.values():
            if value!=0:
                return False
        return True