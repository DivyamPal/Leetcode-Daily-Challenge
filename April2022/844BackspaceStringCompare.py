class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result1=[]
        result2=[]
        for i in range(len(s)):
            if s[i]=="#":
                if s[i]=="#" and not result1:
                    continue
                else:
                    result1.pop()
            else:
                result1.append(s[i])
        print(result1)
        for j in range(len(t)):
            if t[j]=="#":
                if t[j]=="#" and not result2:
                    continue
                else:
                    result2.pop()
            else:
                result2.append(t[j])
        print(result2)        
        
        if result1==result2:
            return True
        else:
            return False
