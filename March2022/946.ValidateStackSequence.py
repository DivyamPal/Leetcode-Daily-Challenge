class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]  
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while len(stack)>0 and len(popped)>0 and popped[0]==stack[-1]:
                stack.pop()
                popped.pop(0)
            
        print(stack)
        print(popped)
        if stack==popped[::-1]: return True
        else: return False
