class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in range(len(s)):
            if len(stack)>0 and s[i]==stack[-1][0] :
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([s[i],1])
        print(stack)
        result=""
        for i in range(len(stack)):
            result+=stack[i][0]*stack[i][1]
        return result
