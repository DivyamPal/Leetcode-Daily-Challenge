class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        ls=[]
        n=len(t)
        if (s==""):
            return True
        while i<n:
            while j<len(s):
                if(i==n):
                    break
                elif(s[j]==t[i]):
                    ls.append(t[i])
                    i+=1
                    j+=1
                else:
                    i+=1
            i+=1
        ls1=""
        if(ls1.join(ls)==s):
            return True
        else:
            return False
