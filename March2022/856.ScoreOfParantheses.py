class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                top=stack.pop()
                if i==')' and top=='(':
                    stack.append(1)
                else:
                    score=0
                    while top!='(':
                        score+=top
                        top=stack.pop()
                    stack.append(2*score)
        print(stack)
        return sum(stack)
