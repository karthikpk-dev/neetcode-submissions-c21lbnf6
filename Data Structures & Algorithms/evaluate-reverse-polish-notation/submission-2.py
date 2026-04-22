class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            match x:
                case '+':
                    stack.append(stack.pop()+stack.pop())
                case '-':
                    stack.append(-stack.pop()+stack.pop())
                case '*':
                    stack.append(stack.pop()*stack.pop())
                case '/':
                    x=stack.pop()
                    y=stack.pop()
                    stack.append(int(y/x))
                case _:
                    stack.append(int(x))
        return stack[-1]
            
