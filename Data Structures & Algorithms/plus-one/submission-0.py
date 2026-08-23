class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        c=1
        for i in range(len(digits)-1,-1,-1):
            s=c+digits[i]
            if s<10:
                res.append(s)
                c=0
            else:
                res.append(int(s%10))
                c=int(s/10)
        if c:
            res.append(int(c))
        res.reverse()
        return res
