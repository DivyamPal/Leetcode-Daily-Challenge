class Solution:
    def isValid(self, s: str) -> bool:
        pairs_dict={')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i not in pairs_dict:
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != pairs_dict[i]:
                return False
        if len(stack) == 0:
            return True
