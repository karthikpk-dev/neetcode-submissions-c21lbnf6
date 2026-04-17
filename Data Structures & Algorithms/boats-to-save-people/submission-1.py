class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        i,j=0,n-1
        people.sort()
        res=0
        while i<=j:
            if people[i]+people[j]<=limit:
                
                i+=1
                
            j-=1
            res+=1
        return res

