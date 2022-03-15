class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res=list(s)
        stack = []
        for i in range(len(res)):
            if res[i] == "(":
                stack.append(i)
            elif res[i] == ")":
                if len(stack):
                    stack.pop()
                else:
                    res[i]=''
        print(res)
        # print(stack)
        for i in stack:
            res[i] = ""
        return "".join(res)

    
    
