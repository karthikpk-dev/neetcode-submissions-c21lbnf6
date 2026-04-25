class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        x=[]
        for i in range(len(position)):
            x.append((position[i],speed[i]))
        x.sort(reverse= True)
        for i in range(len(x)):
            if not stack:
                stack.append((target - x[i][0] )/ x[i][1])
                continue
            if (target - x[i][0])/x[i][1] <=stack[-1]:
                continue
            else:
                stack.append((target - x[i][0]) / x[i][1])
        return len(stack)
