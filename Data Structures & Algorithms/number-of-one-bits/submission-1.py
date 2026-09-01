class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            rem=n%2
            if rem:
                count+=1
            n=n//2
        return count
