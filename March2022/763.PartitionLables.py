class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        res=[]
        start,end=0,0
        for i in range(len(s)):
            dic[s[i]]=i
        for i in range(len(s)):
            end=max(end,dic[s[i]])
            if end==i:
                res.append(end-start+1)
                start=i+1
        return res
    
    
  
