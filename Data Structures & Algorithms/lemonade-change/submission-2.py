class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for x in bills:
            if x==5:
                five+=1
            elif x==10:
                ten+=1
                if five:               
                    five-=1
                else:
                    return False
            else:
                if five>=3:
                    five-=3
                elif five and ten:
                    ten-=1
                    five-=1
                else:
                    return False
        return True
                