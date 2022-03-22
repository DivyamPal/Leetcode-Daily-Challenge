class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res=''
        while (n-1)*26 >=k:
            res+='a'
            n-=1;k-=1
        res+=chr(ord('a')+(k % 26 or 26)-1)
        res+='z'*(n-1)
        return res
