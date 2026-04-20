class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        sum=0
        for i in range(len(operations)):
            if operations[i] == '+' and len(stack)>1:
                stack.append(stack[-1]+stack[-2])
            elif operations[i] == 'D' and len(stack)>0:
                stack.append(stack[-1]*2)
            elif operations[i] == 'C' and len(stack)>0:
                stack.pop()
            else:
                stack.append(int(operations[i]))
            
        for x in stack:
            sum+=x
        return sum