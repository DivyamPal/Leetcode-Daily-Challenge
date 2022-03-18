class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic=Counter(s)
        stack=[]
        for i in s:
            if i in stack:
                dic[i]-=1
                continue
            while len(stack) > 0 and stack[-1] > i and dic[stack[-1]] > 0:
                stack.pop()
            dic[i]-=1
            stack.append(i) 
        return "".join(stack)
