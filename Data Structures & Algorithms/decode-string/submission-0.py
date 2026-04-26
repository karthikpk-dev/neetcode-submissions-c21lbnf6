class Solution:
    def decodeString(self, s: str) -> str:
        curr_num=0
        curr_str=''
        stack=[]
        for x in s:
            if x.isalpha():
                curr_str+=x
            elif x.isdigit():
                curr_num= 10 * curr_num +int(x)
            elif x=='[':
                stack.append((curr_str,curr_num))
                curr_str=''
                curr_num=0
            else:
                y=stack.pop()
                curr_str=y[0] + curr_str*y[1]
        return curr_str
