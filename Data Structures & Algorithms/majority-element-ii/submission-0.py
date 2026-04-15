class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,cand2=-1,-1
        count1,count2=0,0

        for x in nums:
            if x==cand1:
                count1+=1
            elif x==cand2:
                count2+=1
            elif count1==0:
                cand1=x
                count1=1
            elif count2==0:
                cand2=x
                count2=1
            else:
                count1-=1
                count2-=1
        count1=count2=0
        n=len(nums)
        for x in nums:
            if x == cand1:
                count1+=1
            if x == cand2:
                count2+=1
        
        return [cand1,cand2] if count1>n//3 and count2>n//3 else [cand1] if count1>n//3 else [cand2] if count2>n//3 else []
